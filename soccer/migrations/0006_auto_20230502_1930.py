# Generated by Django 3.2.10 on 2023-05-02 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0005_auto_20230502_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='birthday_new',
            new_name='birthday',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='birthday_new',
            new_name='birthday',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='foot_new',
            new_name='foot',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='height_new',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='year_established_new',
            new_name='year_established',
        ),
    ]
