# Generated by Django 4.0.5 on 2023-05-19 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headcount',
            name='coordinate',
            field=models.JSONField(default=[0.0, 0.0]),
        ),
    ]