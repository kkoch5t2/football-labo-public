# Generated by Django 3.2.10 on 2023-09-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0038_alter_customuser_change_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_icon',
            field=models.ImageField(blank=True, null=True, upload_to='user_icon/'),
        ),
    ]
