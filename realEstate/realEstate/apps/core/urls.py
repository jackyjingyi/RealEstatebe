from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import ManageFilesViewSets

router = DefaultRouter()
router.register(r'management', ManageFilesViewSets, basename='management')

urlpatterns = [
    path('', include(router.urls)),

]
