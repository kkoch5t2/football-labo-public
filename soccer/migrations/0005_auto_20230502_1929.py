# Generated by Django 3.2.10 on 2023-05-02 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0004_auto_20230424_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='player',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='player',
            name='foot',
        ),
        migrations.RemoveField(
            model_name='player',
            name='height',
        ),
        migrations.RemoveField(
            model_name='team',
            name='year_established',
        ),
    ]
