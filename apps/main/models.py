# Python
from typing import Any

# Django
from django.db import models
from django.db.models.query import QuerySet


class Stadium(models.Model):
    """Stadium."""

    title = models.CharField(
        max_length=25,
        verbose_name='название'
    )
    capacity = models.IntegerField(
        verbose_name='вместимость'
    )
    city = models.CharField(
        max_length=25,
        verbose_name='город'
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'стадион'
        verbose_name_plural = 'стадионы'

    def __str__(self) -> str:
        return self.title


class Team(models.Model):
    """Team."""

    title = models.CharField(
        max_length=25,
        verbose_name='название'
    )
    stadium = models.ForeignKey(
        Stadium,
        on_delete=models.RESTRICT,
        verbose_name='стадион'
    )

    class Meta:
        ordering = (
            '-id',
        )
        verbose_name = 'команда'
        verbose_name_plural = 'команды'

    def __str__(self) -> str:
        return self.title


class PlayerManager(models.Manager):

    def get_free_agents(self) -> QuerySet['Player']:
        return self.filter(
            status=Player.FREE_AGENT
        )

    def get_team_members(self) -> QuerySet['Player']:
        return self.filter(
            status=Player.TEAM_MEMBER
        )

    def get_young_players(self) -> QuerySet['Player']:
        return self.filter(
            status=Player.TEAM_MEMBER,
            age__lt=Player.MIN_AGE_FOR_ADULT_TEAM,
            power__lte=Player.MIN_POWER_FOR_ADULT_TEAM
        )


class Player(models.Model):
    """Player."""

    MIN_AGE_FOR_ADULT_TEAM: int = 21
    MIN_POWER_FOR_ADULT_TEAM: int = 50
    FREE_AGENT: int = 0
    TEAM_MEMBER: int = 1
    STATUSES: tuple[tuple[int, str], ...] = (
        (FREE_AGENT, 'Свободный агент'),
        (TEAM_MEMBER, 'Состоит в команде')
    )

    name = models.CharField(
        max_length=25,
        verbose_name='имя'
    )
    surname = models.CharField(
        max_length=25,
        verbose_name='фамилия'
    )
    power = models.IntegerField(
        verbose_name='сила'
    )
    age = models.IntegerField(
        verbose_name='возраст'
    )
    status = models.SmallIntegerField(
        choices=STATUSES,
        default=FREE_AGENT,
        verbose_name='статус'
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
        related_name='players',
        verbose_name='команда'
    )
    objects = PlayerManager()

    class Meta:
        ordering = (
            '-power',
        )
        verbose_name = 'игрок'
        verbose_name_plural = 'игроки'

    def save(
        self,
        *args: Any,
        **kwargs: Any
    ) -> None:
        super().save(*args, **kwargs)

    def delete(self) -> None:
        self.status = self.FREE_AGENT
        self.save(
            update_fields=('status',)
        )

    def __str__(self) -> str:
        return f'{self.name} {self.surname} | {self.power}'
