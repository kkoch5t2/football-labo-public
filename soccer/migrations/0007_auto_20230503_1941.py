# Generated by Django 3.2.10 on 2023-05-03 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0006_auto_20230502_1930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeamUpdateRequest',
            new_name='ClubUpdateRequest',
        ),
        migrations.RenameModel(
            old_name='CountryUpdateRequest',
            new_name='NationalUpdateRequest',
        ),
    ]
