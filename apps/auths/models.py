# Django
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class ClientManager(BaseUserManager):

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class Client(AbstractBaseUser, PermissionsMixin):
    """Custom."""

    email = models.EmailField(
        max_length=100, unique=True, verbose_name='почта'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='активность'
    )
    is_superuser = models.BooleanField(
        default=False, verbose_name='администратор'
    )
    is_staff = models.BooleanField(
        default=False, verbose_name='менеджер'
    )
    date_joined = models.DateTimeField(
        default=timezone.now, verbose_name='дата регистрации'
    )
    balance = models.FloatField(
        default=0.0, verbose_name='баланс'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ClientManager()

    class Meta:
        ordering = (
            '-date_joined',
        )
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
