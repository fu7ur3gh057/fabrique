from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


API_URL = 'api/v3'

schema_view = get_schema_view(
    openapi.Info(
        title="Fabrique API",
        default_version='v1',
        description="Distribution Message API",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="fu7ur3gh057@gmail.com.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f'{API_URL}/client/', include('apps.client.api.urls')),
    path(f'{API_URL}/distribute/', include('apps.distribution.api.urls')),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
