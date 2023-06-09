# Generated by Django 4.1.5 on 2023-05-11 12:36

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
            name="category",
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
                ("category_name", models.CharField(max_length=50)),
                ("category_status", models.CharField(max_length=10)),
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
                ("quantity", models.CharField(max_length=500)),
                ("price", models.IntegerField()),
                ("order_status", models.CharField(max_length=10)),
            ],
        ),
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
                ("image", models.ImageField(upload_to="images")),
                ("stock", models.CharField(max_length=500)),
                ("product_status", models.CharField(max_length=10)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="payment",
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
                ("amount", models.CharField(max_length=10)),
                ("date", models.DateField()),
                ("paymentstatus", models.CharField(max_length=10)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="brookwoodapp.order",
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
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="brookwoodapp.product"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="brookwoodapp.brookuser"
            ),
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
                ("product", models.CharField(max_length=500)),
                ("complaint", models.CharField(max_length=500)),
                ("date", models.DateField()),
                ("replay", models.CharField(default="No Replay", max_length=500)),
                ("complaint_status", models.CharField(max_length=10)),
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
                ("quantity", models.CharField(max_length=500)),
                ("total_price", models.CharField(max_length=500)),
                ("cart_status", models.CharField(max_length=10)),
                ("image", models.ImageField(upload_to="images")),
                ("category", models.CharField(max_length=10)),
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
