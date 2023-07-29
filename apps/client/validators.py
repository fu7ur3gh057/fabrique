from django.core.exceptions import ValidationError
from rest_framework import serializers


def validate_starts_with_7(value) -> None:
    if not str(value).startswith('7'):
        raise ValidationError("The value must start with 7.")


def serializer_validate_starts_with_7(value) -> None:
    if not str(value).startswith('7'):
        raise serializers.ValidationError("The value must start with 7.")


def validate_ten_digits(value: int) -> None:
    if not (10000000000 <= value <= 99999999999):
        raise ValidationError('length of phone_number should be equal 11')


def serializer_validate_ten_digits(value: int) -> None:
    if not (10000000000 <= value <= 99999999999):
        raise serializers.ValidationError('length of phone_number should be equal 11')


def validate_three_digits(value: int) -> None:
    if not (100 <= value <= 999):
        raise ValidationError('length of operator_code should be equal 3')


def serializer_validate_three_digits(value: int) -> None:
    if not (100 <= value <= 999):
        raise serializers.ValidationError('length of operator_code should be equal 3')
