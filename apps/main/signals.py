# Python
from typing import Any

# Django
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.base import ModelBase
from django.db.models.signals import (
    post_delete,
    post_save
)
from django.dispatch import receiver

# Local
from .models import Player


@receiver(
    post_save,
    sender=Player
)
def post_save_player(
    sender: ModelBase,
    instance: Player,
    created: bool,
    **kwargs: Any
) -> None:
    """Post-save Player."""
    if created:
        send_mail(
            f'Новый игрок: {instance.fullname}',
            f'Доступен новый игрок на трансферном рынке: {instance}',
            settings.EMAIL_HOST_USER,
            ['teweb98233@vingood.com'],
            fail_silently=False
        )
        return

    if instance.status == Player.STATUS_FREE_AGENT:
        send_mail(
            f'Свободный агент: {instance.fullname}',
            f'Доступен игрок на трансферном рынке: {instance}',
            settings.EMAIL_HOST_USER,
            ['teweb98233@vingood.com'],
            fail_silently=False
        )
        return

    if instance.status == Player.STATUS_RETIRED:
        send_mail(
            f'Завершил карьеру: {instance.fullname}',
            f'Игрок завершил карьеру: {instance}',
            settings.EMAIL_HOST_USER,
            ['teweb98233@vingood.com'],
            fail_silently=False
        )
        return


@receiver(
    post_delete,
    sender=Player
)
def post_delete_player(
    sender: ModelBase,
    instance: Player,
    **kwargs: Any
) -> None:
    """Post-delete Player."""
    pass
