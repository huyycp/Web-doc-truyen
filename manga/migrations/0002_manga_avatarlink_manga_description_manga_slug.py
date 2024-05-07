# Generated by Django 5.0.4 on 2024-05-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("manga", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="manga",
            name="avatarLink",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="manga",
            name="description",
            field=models.TextField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="manga",
            name="slug",
            field=models.SlugField(default="", max_length=100, unique=True),
        ),
    ]
