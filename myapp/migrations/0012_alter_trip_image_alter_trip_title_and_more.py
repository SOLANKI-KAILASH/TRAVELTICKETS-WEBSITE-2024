# Generated by Django 5.0.6 on 2024-07-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_delete_tourpackage_trip_image_trip_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='image',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AlterField(
            model_name='trip',
            name='title',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='trip',
            name='tripdescription',
            field=models.TextField(default=' '),
        ),
    ]
