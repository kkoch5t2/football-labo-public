# Generated by Django 3.2.10 on 2023-05-03 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0009_auto_20230504_0039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managernewcreaterequest',
            old_name='achievement',
            new_name='achievement_rating',
        ),
        migrations.RenameField(
            model_name='managernewcreaterequest',
            old_name='attack',
            new_name='attack_rating',
        ),
        migrations.RenameField(
            model_name='managernewcreaterequest',
            old_name='defense',
            new_name='defense_rating',
        ),
        migrations.RenameField(
            model_name='managernewcreaterequest',
            old_name='development',
            new_name='development_rating',
        ),
        migrations.RenameField(
            model_name='managernewcreaterequest',
            old_name='management',
            new_name='management_rating',
        ),
        migrations.RenameField(
            model_name='managernewcreaterequest',
            old_name='political',
            new_name='political_rating',
        ),
    ]
