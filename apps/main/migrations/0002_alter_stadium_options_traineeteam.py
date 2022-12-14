# Generated by Django 4.1.3 on 2022-12-23 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stadium',
            options={'ordering': ('-id',), 'verbose_name': 'стадион', 'verbose_name_plural': 'стадионы'},
        ),
        migrations.CreateModel(
            name='TraineeTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='название')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='main.team')),
            ],
            options={
                'verbose_name': 'команда 2',
                'verbose_name_plural': 'команды 2',
                'ordering': ('-id',),
            },
        ),
    ]
