# Generated by Django 4.1.3 on 2022-12-14 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stadium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='название')),
                ('capacity', models.IntegerField(verbose_name='вместимость')),
                ('city', models.CharField(max_length=25, verbose_name='город')),
            ],
            options={
                'verbose_name': 'команда',
                'verbose_name_plural': 'команды',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='название')),
                ('stadium', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.stadium', verbose_name='стадион')),
            ],
            options={
                'verbose_name': 'команда',
                'verbose_name_plural': 'команды',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='имя')),
                ('surname', models.CharField(max_length=25, verbose_name='фамилия')),
                ('power', models.IntegerField(verbose_name='сила')),
                ('age', models.IntegerField(verbose_name='возраст')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.team', verbose_name='команда')),
            ],
            options={
                'verbose_name': 'игрок',
                'verbose_name_plural': 'игроки',
                'ordering': ('-power',),
            },
        ),
    ]
