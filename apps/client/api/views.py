from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from rest_framework.request import Request
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.client.api.serializers import ClientInputSerializer, ClientUpdateSerializer, ClientOutputSerializer
from apps.client.models import Client


# Get List of all Clients Request
class ListClientAPIView(APIView):
    serializer_class = ClientOutputSerializer

    @swagger_auto_schema(responses={200: ClientOutputSerializer(many=False)})
    def get(self, request: Request) -> Response:
        client_list = Client.objects.all()
        serializer_list = self.serializer_class(client_list, many=True)
        return Response(serializer_list.data, status=status.HTTP_200_OK)


# Post Client Request
class CreateClientAPIView(APIView):
    serializer_class = ClientInputSerializer

    @swagger_auto_schema(request_body=ClientInputSerializer)
    def post(self, request: Request) -> Response:
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Patch Client Request
class UpdateClientAPIView(APIView):
    serializer_class = ClientUpdateSerializer
    parser_classes = [MultiPartParser]

    @swagger_auto_schema(request_body=ClientUpdateSerializer, manual_parameters=[
        openapi.Parameter(
            'operator_code',
            openapi.IN_FORM,
            type=openapi.TYPE_INTEGER,
            required=False,
            default=303
        ),
        openapi.Parameter(
            'phone_number',
            openapi.IN_FORM,
            type=openapi.TYPE_INTEGER,
            required=False,
            default=71234567890
        )
    ])
    def patch(self, request: Request, pk_id: int) -> Response:
        client = get_object_or_404(Client, pk_id=pk_id)
        serializer = self.serializer_class(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


# Delete Client Request
class DeleteClientSerializer(APIView):

    def delete(self, request: Request, pk_id: int) -> Response:
        client = get_object_or_404(Client, pk_id=pk_id)
        client.delete()
        return Response(True)
