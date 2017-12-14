from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('zeppelin.urls')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
]
