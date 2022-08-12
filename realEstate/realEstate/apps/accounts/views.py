from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.response import Response
from django.middleware.csrf import get_token


@api_view(['GET'])
@ensure_csrf_cookie
def get_csrf_token(request):
    # 前后端分离业务
    token = get_token(request)
    return Response({'csrf_token': token})