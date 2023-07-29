from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.distribution.api.serializers import DistributionOutputSerializer, DistributionInputSerializer, \
    DistributionUpdateSerializer, DistributionStatisticSerializer, DistributionDetailStatisticSerializer
from apps.distribution.models import Distribution
from utils.datetime_utils import compare_datetime


class ListDistributionAPIView(APIView):
    serializer_class = DistributionOutputSerializer

    @swagger_auto_schema(responses={200: DistributionOutputSerializer(many=False)})
    def get(self, request: Request) -> Response:
        distribution_list = Distribution.objects.all()
        serializer_list = self.serializer_class(distribution_list, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)


class CreateDistributionAPIView(APIView):
    serializer_class = DistributionInputSerializer

    @swagger_auto_schema(request_body=DistributionInputSerializer)
    def post(self, request: Request) -> Response:
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateDistributionAPIView(APIView):
    serializer_class = DistributionUpdateSerializer

    @swagger_auto_schema(request_body=DistributionUpdateSerializer)
    def patch(self, request: Request, pk_id: int) -> Response:
        distribution = get_object_or_404(Distribution, pk_id=pk_id)
        serializer = self.serializer_class(distribution, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteDistributionAPIView(APIView):

    def delete(self, request: Request, pk_id: int) -> Response:
        distribution = get_object_or_404(Distribution, pk_id=pk_id)
        distribution.delete()
        return Response(True)


class StatisticDistributionAPIView(APIView):
    serializer_class = DistributionStatisticSerializer

    @swagger_auto_schema(responses={200: DistributionStatisticSerializer(many=False)})
    def get(self, request: Request) -> Response:
        distribs = Distribution.objects.all()
        serializer_list = self.serializer_class(distribs, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)


class DetailStatisticDistributionAPIView(APIView):
    serializer_class = DistributionDetailStatisticSerializer

    @swagger_auto_schema(responses={200: DistributionDetailStatisticSerializer(many=False)})
    def get(self, request: Request, pk_id: int) -> Response:
        distribution = get_object_or_404(Distribution, pk_id=pk_id)
        serializer = self.serializer_class(distribution)
        return Response(serializer.data, status=status.HTTP_200_OK)

# обработки активных рассылок и отправки сообщений клиентам?????????
