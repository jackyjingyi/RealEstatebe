from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import Protocol1_1ViewSet, Protocol1_2ViewSet, Protocol1_3ViewSet, ProtocolMainViewSet

router = DefaultRouter()

router.register(r'protocol_main', ProtocolMainViewSet, basename='protocol_main')
router.register(r'protocol1_1', Protocol1_1ViewSet, basename='protocol1_1')
router.register(r'protocol1_2', Protocol1_2ViewSet, basename='protocol1_2')
router.register(r'protocol1_3', Protocol1_3ViewSet, basename='protocol1_3')

urlpatterns = [
    path('', include(router.urls))
]
