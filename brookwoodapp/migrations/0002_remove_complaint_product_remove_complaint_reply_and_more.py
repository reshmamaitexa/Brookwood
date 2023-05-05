# Generated by Django 4.1.5 on 2023-05-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brookwoodapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="complaint",
            name="product",
        ),
        migrations.RemoveField(
            model_name="complaint",
            name="reply",
        ),
        migrations.RemoveField(
            model_name="complaint",
            name="time",
        ),
        migrations.AddField(
            model_name="complaint",
            name="replay",
            field=models.CharField(default="No Replay", max_length=500),
        ),
        migrations.AlterField(
            model_name="complaint",
            name="date",
            field=models.DateField(),
        ),
    ]
