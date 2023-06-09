# Generated by Django 4.2 on 2023-05-01 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("keyword", models.CharField(max_length=30)),
                ("distance", models.CharField(max_length=30)),
                ("category", models.CharField(max_length=50)),
                ("location", models.CharField(max_length=50)),
            ],
        ),
    ]
