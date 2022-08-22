# Generated by Django 4.1 on 2022-08-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("family", models.CharField(max_length=50)),
                ("mobile_number", models.CharField(max_length=11, unique=True)),
                ("gender", models.BooleanField(blank=True, default=True, null=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_admin", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]