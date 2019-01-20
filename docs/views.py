from drf_yasg.openapi import Contact, License
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LedsZeppelin API",
        default_version='v1',
        description="Documentação dos endpoint do projeto LedsZeppelin",
        contact=Contact(email="andre.sp.leao@gmail.com"),
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
