# Generated by Django 3.1 on 2020-09-08 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20200907_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='listing',
        ),
    ]