from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.distribution.models import Distribution


@receiver(post_save, sender=Distribution)
def create_message():
    pass
