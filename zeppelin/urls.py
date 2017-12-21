from django.conf.urls import url
from django.conf.urls import include


urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
]
