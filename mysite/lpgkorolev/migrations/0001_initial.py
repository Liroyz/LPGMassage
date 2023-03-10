# Generated by Django 4.1.7 on 2023-03-03 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=254, verbose_name="Название услуги"
                    ),
                ),
            ],
            options={"verbose_name": "Услуга", "verbose_name_plural": "Услуги",},
        ),
        migrations.CreateModel(
            name="Specialist",
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
                    "name",
                    models.CharField(
                        db_index=True, max_length=254, verbose_name="Имя специалиста"
                    ),
                ),
                ("services", models.ManyToManyField(to="lpgkorolev.service")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Специалист",
                "verbose_name_plural": "Специалисты",
            },
        ),
        migrations.CreateModel(
            name="Appointment",
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
                ("first_name", models.CharField(max_length=254, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=254, verbose_name="Фамилия")),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=17, verbose_name="Номер телефона"
                    ),
                ),
                ("fact_date", models.DateTimeField(verbose_name="Дата и время записи")),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lpgkorolev.service",
                        verbose_name="Услуга",
                    ),
                ),
                (
                    "specialist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="lpgkorolev.specialist",
                        verbose_name="Специалист",
                    ),
                ),
            ],
            options={"verbose_name": "Запись", "verbose_name_plural": "Записи",},
        ),
    ]