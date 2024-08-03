# Generated by Django 5.0.6 on 2024-07-28 02:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.IntegerField()),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('passport_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
                ('date_joined', models.DateField()),
                ('last_login', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city')),
            ],
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state'),
        ),
        migrations.CreateModel(
            name='trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_location', models.CharField(max_length=30)),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField()),
                ('price', models.IntegerField()),
                ('available_seats', models.IntegerField()),
                ('total_seats', models.IntegerField()),
                ('trip_type', models.CharField(max_length=30)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.destination')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField()),
                ('no_of_seats', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=30)),
                ('is_available', models.BooleanField()),
                ('created_at', models.DateField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('review_date', models.DateField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.booking')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('payment_method', models.CharField(choices=[('credit card', 'Credit Card'), ('debit card', 'Debit Card'), ('paypal', 'PayPal'), ('other', 'Other')], max_length=30)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=30)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.booking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('sent_date', models.DateField()),
                ('read', models.BooleanField()),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_date', models.DateField()),
                ('available_seats', models.IntegerField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]