# Generated by Django 4.1.5 on 2023-05-05 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="brookuser",
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
                ("fullname", models.CharField(max_length=20)),
                ("housename", models.CharField(max_length=30)),
                ("roadname", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=20)),
                ("state", models.CharField(max_length=20)),
                ("post", models.CharField(max_length=20)),
                ("pincode", models.CharField(max_length=6)),
                ("email", models.EmailField(max_length=40)),
                ("phone_number", models.CharField(max_length=10)),
                ("role", models.CharField(max_length=10)),
                ("userstatus", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Log",
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
                ("username", models.CharField(max_length=20, unique=True)),
                ("password", models.CharField(max_length=20, unique=True)),
                ("role", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="product",
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
                ("product_name", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("GST", models.IntegerField()),
                ("product_price", models.IntegerField()),
                ("product_details", models.CharField(max_length=300)),
                ("stock", models.CharField(max_length=500)),
                ("product_status", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="order",
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
                ("Quantity", models.CharField(max_length=500)),
                ("price", models.IntegerField()),
                ("date", models.CharField(max_length=20)),
                ("time", models.CharField(max_length=20)),
                ("order_status", models.CharField(max_length=10)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="feedback",
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
                ("date", models.CharField(max_length=20)),
                ("time", models.CharField(max_length=20)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.brookuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="complaint",
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
                ("complaint", models.CharField(max_length=500)),
                ("date", models.CharField(max_length=20)),
                ("time", models.CharField(max_length=20)),
                ("reply", models.CharField(max_length=500)),
                ("complaint_status", models.CharField(max_length=10)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.brookuser",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="cart",
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
                ("price", models.IntegerField()),
                ("Quantity", models.CharField(max_length=500)),
                ("cart_status", models.CharField(max_length=10)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.brookuser",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="brookuser",
            name="log_id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="brookwoodapp.log"
            ),
        ),
    ]
