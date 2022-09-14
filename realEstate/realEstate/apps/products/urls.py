from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import BuildingProductViewSet,HouseViewSet

router = DefaultRouter()

router.register(r'buildings', BuildingProductViewSet, basename='buildings')
router.register(r'house', HouseViewSet, basename='house')


urlpatterns = [
    path('', include(router.urls))
]