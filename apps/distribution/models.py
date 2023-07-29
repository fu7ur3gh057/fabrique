from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from django_enum_choices.fields import EnumChoiceField

from apps.client.models import Client
from other.enums import Status


class Distribution(models.Model):
    pk_id = models.BigAutoField(primary_key=True, editable=False)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    text = models.TextField(blank=False)
    filter = ArrayField(models.CharField(max_length=100), blank=False)

    def __str__(self) -> str:
        return f'{self.pk_id}'


class Message(models.Model):
    pk_id = models.BigAutoField(primary_key=True, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    status = EnumChoiceField(Status, default=Status.CREATED, verbose_name=_("Status"))
    distribution = models.ForeignKey(
        Distribution,
        related_name='messages',
        on_delete=models.CASCADE,
        null=False
    )
    client = models.ForeignKey(
        Client,
        related_name='messages',
        on_delete=models.CASCADE,
        null=False
    )
