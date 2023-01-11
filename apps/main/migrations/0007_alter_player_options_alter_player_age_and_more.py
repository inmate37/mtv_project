# Generated by Django 4.1.3 on 2023-01-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_player_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('-id',), 'verbose_name': 'игрок', 'verbose_name_plural': 'игроки'},
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='возраст'),
        ),
        migrations.AlterField(
            model_name='player',
            name='power',
            field=models.PositiveSmallIntegerField(verbose_name='сила'),
        ),
        migrations.AlterField(
            model_name='player',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Свободный агент'), (1, 'Состоит в команде')], default=0, verbose_name='статус'),
        ),
    ]
