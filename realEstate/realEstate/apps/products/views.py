from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BuildingProduct, House
from rest_framework import viewsets
from django_filters import rest_framework as filters
from .models import BuildingProduct, House
from .serializers import BuildingCreateUpdateSerializer, BuildingListSerializer, HouseSerializer, \
    BuildingProductListSerializer, BuildingProductCreateUpdateSerializer, HouseListSerializer, \
    HouseCreateUpdateSerializer


class BuildingProductFilter(filters.FilterSet):
    class Meta:
        model = BuildingProduct
        exclude = ["image", "thumbnail"]


class HouseFilter(filters.FilterSet):
    building_text = filters.CharFilter(field_name="building")

    class Meta:
        model = House
        exclude = ["image", "house_detail", "thumbnail"]


class BuildingProductViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingProductListSerializer
    queryset = BuildingProduct.objects.all().order_by('-pk')
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BuildingProductFilter
    search_fields = ["id", "product_code", "region", "product_type", "staircase_ratio", "house_type_combination",
                     "source", "applicable_area", "residential_type", "building_attr", "core_bucket_feature",
                     "storey_type", "insulation_area", "up_floors", "applicable_product_line", "bucket_pdf",
                     "bucket_dwg"]

    def get_serializer_class(self):
        if self.action == "list":
            return BuildingProductListSerializer
        else:
            return BuildingProductCreateUpdateSerializer

    def list(self, request, *args, **kwargs):
        print(request.query_params)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class HouseViewSet(viewsets.ModelViewSet):
    serializer_class = HouseListSerializer
    queryset = House.objects.all().order_by('-pk')
    filter_class = HouseFilter
    search_fields = ["id", "product_code", "position", "staircase_ratio", "house_type", "source", "bucket_pdf",
                     "bucket_dwg"]

    def get_serializer_class(self):
        if self.action == "list":
            return HouseListSerializer
        else:
            return HouseCreateUpdateSerializer
