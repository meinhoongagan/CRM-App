# Generated by Django 4.2.6 on 2023-12-11 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_team'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
    ]
