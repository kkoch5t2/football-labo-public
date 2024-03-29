# Generated by Django 3.2.10 on 2023-04-09 12:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0002_countryupdaterequest_managerupdaterequest_playerupdaterequest_teamupdaterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='birthday_new',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='birthday_new',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='foot_new',
            field=models.CharField(choices=[('右足', '右足'), ('左足', '左足')], default='右足', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='height_new',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='year_established_new',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
