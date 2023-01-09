# Generated by Django 4.1.3 on 2023-01-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_player_team_alter_team_stadium_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Свободный агент'), (1, 'Состоит в команде')], default=0, verbose_name='статус'),
        ),
    ]
