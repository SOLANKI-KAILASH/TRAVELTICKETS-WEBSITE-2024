# Generated by Django 5.0.6 on 2024-08-01 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0032_rename_trip_trips_rename_booktrip_bookings_trip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='trips',
            new_name='trip',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='trip',
            new_name='booktrip',
        ),
    ]
