# Generated by Django 5.0.6 on 2024-07-31 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_alter_trip_tripno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='tripno',
        ),
    ]
