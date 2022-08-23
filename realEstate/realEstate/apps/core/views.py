from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import ManagementFiles, Materials
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .serializers import ManagementFilesSerializer, MaterialsSerializers
from rest_framework.permissions import DjangoObjectPermissions, DjangoModelPermissions, \
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated


class ManagementFilter(filters.FilterSet):
    class Meta:
        model = ManagementFiles
        exclude = ['file', 'download_file']


class MaterialsFilter(filters.FilterSet):
    class Meta:
        model = Materials
        exclude = ['file']


class ManageFilesViewSets(viewsets.ModelViewSet):
    queryset = ManagementFiles.objects.all()
    serializer_class = ManagementFilesSerializer
    # pagination_class = SmallResultsSetPagination
    filterset_class = ManagementFilter
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class MaterialsViewSets(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializers
    filterset_class = MaterialsFilter
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class NavList(APIView):

    def get(self, request, format=None):
        data = {
            'user': request.user.id,
            'permission': [],
            'depth': 3,
            'data': [
                {
                    'lv1_label': '标准化管理工具',
                    'seq': 0,
                    'items': [
                        {
                            'label': '集团地产产品库V1.0管理办法',
                            'items': [
                                {
                                    {
                                        # 'id':''
                                        # 'label': '附件1：集团地产产品库V1.0管理办法（试行）',

                                    }
                                }
                            ]
                        }
                    ]
                }
            ]
        }
