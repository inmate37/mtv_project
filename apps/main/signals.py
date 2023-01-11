# Python
from typing import Any

# Django
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.base import ModelBase
from django.db.models.signals import post_save
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
    *args: Any,
    **kwargs: Any
) -> None:
    """Post-save Player."""
    send_mail(
        'Новый свободный агент',
        'Доступен новый игрок на трансферном рынке',
        settings.EMAIL_HOST_USER,
        [
            'kobit53104@webonoid.com'
        ],
        fail_silently=False
    )
