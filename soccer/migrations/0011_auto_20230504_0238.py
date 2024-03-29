# Generated by Django 3.2.10 on 2023-05-03 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0010_auto_20230504_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubnewcreaterequest',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='managernewcreaterequest',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='nationalnewcreaterequest',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='playernewcreaterequest',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='clubcomment',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='managercomment',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='nationalcomment',
            name='user_ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
