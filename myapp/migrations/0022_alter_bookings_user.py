# Generated by Django 5.0.6 on 2024-07-31 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_rename_userdetails_bookings_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='user',
            field=models.CharField(max_length=30),
        ),
    ]