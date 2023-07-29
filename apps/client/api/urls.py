from django.urls import path
from apps.client.api.views import *

urlpatterns = [
    path("", ListClientAPIView.as_view(), name='client-list'),
    path("create/", CreateClientAPIView.as_view(), name='client-create'),
    path("update/<pk_id>/", UpdateClientAPIView.as_view(), name='client-update'),
    path("delete/<pk_id>/", DeleteClientSerializer.as_view(), name='client-delete'),
]
