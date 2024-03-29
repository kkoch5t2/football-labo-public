# Generated by Django 3.2.10 on 2023-08-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0028_auto_20230622_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackIp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('reason', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'ブロック対象のIP',
            },
        ),
    ]
