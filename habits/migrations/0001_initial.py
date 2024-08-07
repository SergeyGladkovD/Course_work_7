# Generated by Django 5.1 on 2024-08-07 19:34

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        max_length=100, verbose_name="Место выполнения привычки"
                    ),
                ),
                (
                    "time",
                    models.DateTimeField(verbose_name="Начало выполнения привычки"),
                ),
                ("action", models.TextField(verbose_name="Что нужно сделать")),
                (
                    "pleasant_habit_sign",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "periodicity",
                    models.SmallIntegerField(default=1, verbose_name="Периодичность"),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="Награда за выполнение",
                    ),
                ),
                (
                    "duration",
                    models.DurationField(
                        default=datetime.timedelta(seconds=120),
                        verbose_name="Продолжительность выполнения",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публикации"
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
