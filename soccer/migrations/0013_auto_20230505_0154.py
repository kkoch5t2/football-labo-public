# Generated by Django 3.2.10 on 2023-05-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0012_auto_20230504_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubnewcreaterequest',
            name='year_established',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='playernewcreaterequest',
            name='height',
            field=models.IntegerField(),
        ),
    ]