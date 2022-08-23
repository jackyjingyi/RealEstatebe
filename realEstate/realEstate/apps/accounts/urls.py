from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import get_csrf_token, UserDisplayViews,UserCreateView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('get_csrf_token', get_csrf_token),
    path('user_list', UserDisplayViews.as_view()),
    path('bulk_create', UserCreateView.as_view())
]
