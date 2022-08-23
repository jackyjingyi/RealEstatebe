from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import ManageFilesViewSets,MaterialsViewSets

router = DefaultRouter()
router.register(r'management', ManageFilesViewSets, basename='management')
router.register(r'materials', MaterialsViewSets, basename='materials')

urlpatterns = [
    path('', include(router.urls)),

]
