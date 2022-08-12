from django.shortcuts import render
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import ManagementFiles
from .serializers import ManagementFilesSerializer
from rest_framework.permissions import DjangoObjectPermissions, DjangoModelPermissions, \
    DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated


class ManagementFilter(filters.FilterSet):
    class Meta:
        model = ManagementFiles
        exclude = ['file']

class ManageFilesViewSets(viewsets.ModelViewSet):
    queryset = ManagementFiles.objects.all()
    serializer_class = ManagementFilesSerializer
    # pagination_class = SmallResultsSetPagination
    filterset_class = ManagementFilter
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]