# Generated by Django 5.0.4 on 2024-05-30 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_photo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='photo_2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
