from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BuildingProduct, House
from rest_framework import viewsets
from .models import BuildingProduct, House
from .serializers import BuildingCreateUpdateSerializer, BuildingListSerializer


