# Generated by Django 5.0.6 on 2024-08-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_rename_tripname_review_reviewtrip'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review',
            new_name='reviews',
        ),
    ]
