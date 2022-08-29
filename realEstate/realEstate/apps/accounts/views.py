from django.shortcuts import render
from rest_framework.decorators import api_view, action
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from django.middleware.csrf import get_token
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .config import RoleChoices
from .models import IAMUser
from .serializers import UserSerializer, UserUploadSerializer

User = get_user_model()


@api_view(['GET'])
@ensure_csrf_cookie
def get_csrf_token(request):
    # 前后端分离业务
    token = get_token(request)
    return Response({'csrf_token': token})


class UserDisplayViews(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset()).exclude(
            id='1'
        )
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUploadSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        print(type(request.data))
        data = request.data
        # if request.user.is_admin:
        #     # 判断是admin用户
        for u in data:
            try:
                print(u)
                tmp = IAMUser(
                    username=u.get('username'),
                    password=u.get('password'),
                    access_key=u.get('access_key'),
                    secret_key=u.get('secret_key'),
                    role=u.get('role')
                )
                tmp.save()
                serializer = self.get_serializer(data=u)
                serializer.is_valid(raise_exception=True)
                instance = serializer.save()
                print(instance)
                instance.set_password(str(u.get('password')))
                instance.iam_account.add(tmp)
                instance.save()
            except Exception as e:
                print(e)
                continue

        return Response({'msg': 'ok'}, status=200)
