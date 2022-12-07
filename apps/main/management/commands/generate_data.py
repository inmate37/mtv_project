# Python
import random
from typing import Any
from datetime import datetime

# Third party
import names

# Django
from django.core.management.base import BaseCommand

# First party
from auths.models import Client
from main.models import (
    Player,
    Team
)


class Command(BaseCommand):
    """Custom command for filling up database.

    Test data only
    """
    help = 'Custom command for filling up database.'

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_admin(self) -> None:
        """Generates Admin."""

        admin: dict[str, str] = {
            'email': 'root@mail.cc',
            'password': '123'
        }
        if not Client.objects.filter(email=admin['email']).exists():
            Client.objects.create_superuser(
                email=admin['email'],
                password=admin['password']
            )

    def _generate_teams(self) -> None:
        """Generates Teams."""

        titles: tuple[str, ...] = (
            'Bayern Munich',
            'Real Madrid',
            'Barcelona',
            'Juventus',
            'Inter',
            'Milan',
            'Manchester United',
            'Liverpool',
            'Arsenal',
            'Chelsea'
        )
        title: str
        for title in titles:
            obj: dict[str, str] = {
                'title': title
            }
            Team.objects.get_or_create(**obj)

    def _generate_players(self) -> None:
        """Generates Players."""

        total_players: int = 108
        _: int
        for _ in range(total_players):
            obj: dict[str, str | int] = {
                'name': names.get_first_name(gender='male'),
                'surname': names.get_last_name(),
                'power': random.randrange(5, 11)
            }
            Player.objects.get_or_create(**obj)

        Player.objects.get_or_create(
            name='Cristiano',
            surname='Ronaldo',
            power=20
        )
        Player.objects.get_or_create(
            name='Lionel',
            surname='Messi',
            power=20
        )

    def _assign_players_to_teams(self) -> None:
        """Assignes Players to Teams."""

        free_agents: list[Player] = [
            player for player in Player.objects.get_free_agents()
        ]
        team: Team
        for team in Team.objects.get_incomplete_teams():
            count: int = team.players.count()
            while count < Team.PLAYERS_COUNT:
                player: Player = random.choice(free_agents)
                team.players.add(player)
                free_agents.remove(player)
                count += 1

    def handle(self, *args: Any, **kwargs: Any) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()
        self._generate_admin()
        self._generate_teams()
        self._generate_players()
        self._assign_players_to_teams()
        print(
            f'Generated in: {(datetime.now()-start).total_seconds()} seconds'
        )
