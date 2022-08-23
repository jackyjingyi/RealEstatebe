import json, logging
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from guardian.shortcuts import assign_perm, get_users_with_perms, get_user_perms, remove_perm, get_perms
from guardian.core import ObjectPermissionChecker
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import action
from rest_framework.reverse import reverse
from rest_framework.permissions import DjangoObjectPermissions, DjangoModelPermissions, \
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import status
from guardian.shortcuts import assign_perm
from .models import ProtocolMain, Protocol1_1, Protocol1_2, Protocol1_3
from .serializers import Protocol1_1Serializers, Protocol1_2Serializers, Protocol1_3Serializers, ProtocolMainSerializers


class ProtocolMainFilter(filters.FilterSet):
    creator_text = filters.CharFilter(field_name="creator")
    part1_p1_text = filters.CharFilter(field_name="part1_p1")
    part1_p2_text = filters.CharFilter(field_name="part1_p2")
    part1_p3_text = filters.CharFilter(field_name="part1_p3")

    class Meta:
        model = ProtocolMain
        exclude = []


class Protocol1_1Filter(filters.FilterSet):
    creator_text = filters.CharFilter(field_name="creator")

    class Meta:
        model = Protocol1_1
        exclude = ["gov_file", "map_image", "map_cad"]


class Protocol1_2Filter(filters.FilterSet):
    creator_text = filters.CharFilter(field_name="creator")

    class Meta:
        model = Protocol1_2
        exclude = []


class Protocol1_3Filter(filters.FilterSet):
    creator_text = filters.CharFilter(field_name="creator")

    class Meta:
        model = Protocol1_3
        exclude = ["file"]


class ProtocolMainViewSet(viewsets.ModelViewSet):
    queryset = ProtocolMain.objects.all()
    serializer_class = ProtocolMainSerializers
    filterset_class = ProtocolMainFilter
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)




class Protocol1_1ViewSet(viewsets.ModelViewSet):
    queryset = Protocol1_1.objects.all()
    serializer_class = Protocol1_1Serializers
    filterset_class = Protocol1_1Filter

    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_structure(self):
        # 获取前端展示的json
        pass


class Protocol1_2ViewSet(viewsets.ModelViewSet):
    queryset = Protocol1_2.objects.all()
    serializer_class = Protocol1_2Serializers
    filterset_class = Protocol1_2Filter
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class Protocol1_3ViewSet(viewsets.ModelViewSet):
    queryset = Protocol1_3.objects.all()
    serializer_class = Protocol1_3Serializers
    filterset_class = Protocol1_3Filter
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
