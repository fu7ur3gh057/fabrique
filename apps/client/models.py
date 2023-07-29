from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from timezone_field import TimeZoneField

from apps.client.validators import validate_starts_with_7, validate_ten_digits, validate_three_digits


class Client(models.Model):
    pk_id = models.BigAutoField(primary_key=True, editable=False)
    operator_code = models.IntegerField(
        validators=[validate_three_digits],
        help_text="Введите значение из 3 цифр."
    )
    phone_number = models.BigIntegerField(
        validators=[validate_starts_with_7, validate_ten_digits],
        unique=True,
    )
    tag = models.CharField(max_length=100, blank=True, null=True)
    timezone = TimeZoneField(default="Europe/Moscow")

    def __str__(self):
        return f'{self.phone_number}'
