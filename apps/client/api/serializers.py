from collections import OrderedDict

from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

from apps.client.models import Client
from apps.client.validators import validate_three_digits, validate_ten_digits, validate_starts_with_7, \
    serializer_validate_starts_with_7, serializer_validate_three_digits, serializer_validate_ten_digits


class ClientOutputSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    timezone = TimeZoneSerializerField()

    class Meta:
        model = Client
        fields = '__all__'


class ClientInputSerializer(serializers.ModelSerializer):
    pk_id = serializers.IntegerField(read_only=True)
    timezone = TimeZoneSerializerField(default='Europe/Moscow')

    class Meta:
        model = Client
        fields = [
            'pk_id',
            'operator_code',
            'phone_number',
            'tag',
            'timezone',
        ]

    def save(self, **kwargs: dict) -> Client:
        return super().save(**kwargs)


class ClientUpdateSerializer(serializers.ModelSerializer):
    operator_code = serializers.IntegerField(validators=[serializer_validate_three_digits])
    phone_number = serializers.IntegerField(validators=[serializer_validate_ten_digits,
                                                        serializer_validate_starts_with_7])
    tag = serializers.CharField(required=False)
    timezone = TimeZoneSerializerField(required=False)

    class Meta:
        model = Client
        fields = [
            'operator_code',
            'phone_number',
            'tag',
            'timezone',
        ]

    def update(self, instance: Client, validated_data: dict) -> Client:
        super().update(instance=instance, validated_data=validated_data)
        return instance
