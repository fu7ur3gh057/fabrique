from django.urls import path
from apps.distribution.api.views import *

urlpatterns = [
    path("", ListDistributionAPIView.as_view(), name='distribution-list'),
    path("create/", CreateDistributionAPIView.as_view(), name='distribution-create'),
    path("update/<pk_id>/", UpdateDistributionAPIView.as_view(), name='distribution-update'),
    path("delete/<pk_id>/", DeleteDistributionAPIView.as_view(), name='distribution-delete'),
    path("statistic/", StatisticDistributionAPIView.as_view(), name='distribution-statistic'),
    path("statistic/<pk_id>/", DetailStatisticDistributionAPIView.as_view(), name='distribution-statistic-detail'),
]
