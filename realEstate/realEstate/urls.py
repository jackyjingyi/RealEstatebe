from datetime import datetime
from django.contrib import admin
from django.urls import path, include, re_path
from tyadmin_api.views import AdminIndexView
from django.conf.urls.static import static
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


class AppTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['uname'] = user.name
        token['nbf'] = int(round(datetime.timestamp(datetime.now()), 0))
        token['org_exp'] = ''
        token['org_code'] = user.company.org_code if user.company else ''
        token['org_name'] = user.company.name if user.company else ''
        token['avatar'] = None
        token['super'] = 0
        token['is_senior'] = 0
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = AppTokenSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^xadmin/.*', AdminIndexView.as_view()),
    path('api/xadmin/v1/', include('tyadmin_api.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/accounts/', include('realEstate.apps.accounts.urls')),
    path('api/projects/', include('realEstate.apps.projects.urls')),
    path('api/core/',include('realEstate.apps.core.urls')),
    path('api/products/',include('realEstate.apps.products.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
