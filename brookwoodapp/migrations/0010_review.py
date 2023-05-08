# Generated by Django 4.1.5 on 2023-05-07 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("brookwoodapp", "0009_alter_product_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("feedback", models.CharField(max_length=500)),
                ("rating", models.CharField(max_length=50)),
                ("date", models.DateField()),
                ("review_status", models.CharField(max_length=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.brookuser",
                    ),
                ),
            ],
        ),
    ]
