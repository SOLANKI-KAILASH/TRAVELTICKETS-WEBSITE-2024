# Generated by Django 5.0.6 on 2024-07-31 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_trip_bookings_booktrip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='booktrip',
            new_name='trip',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='user',
            new_name='userdetails',
        ),
    ]