# Generated by Django 4.1.5 on 2023-05-30 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brookwoodapp", "0010_order_price_price_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="orders",
        ),
        migrations.AlterField(
            model_name="payment",
            name="paymentstatus",
            field=models.CharField(default="0", max_length=10),
        ),
    ]
