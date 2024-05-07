# Generated by Django 5.0.4 on 2024-05-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("genre", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="genre",
            name="slug",
            field=models.SlugField(default="", max_length=60),
        ),
        migrations.AlterField(
            model_name="genre",
            name="genreName",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
