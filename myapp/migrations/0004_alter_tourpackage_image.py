# Generated by Django 5.0.6 on 2024-07-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_tourpackage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpackage',
            name='image',
            field=models.TextField(),
        ),
    ]