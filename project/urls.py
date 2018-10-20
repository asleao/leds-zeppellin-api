from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('zeppelin.urls')),
    url(r'^api/v1/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/login/', obtain_jwt_token),
    url(r'^api/v1/login/refresh', refresh_jwt_token),
]
