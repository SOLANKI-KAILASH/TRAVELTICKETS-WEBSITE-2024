# Generated by Django 5.0.6 on 2024-07-31 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_rename_booktrip_bookings_trip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='trip',
            new_name='booktrip',
        ),
        migrations.AlterField(
            model_name='bookings',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
