# Generated by Django 3.2.10 on 2023-09-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0036_auto_20230831_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='change_email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
