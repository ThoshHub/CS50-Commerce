# Generated by Django 3.1 on 2020-09-05 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20200905_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('FASHION', 'Fashion'), ('TOYS', 'Toys'), ('ELECTRONICS', 'Electronics'), ('HOME', 'Home'), ('SPORTS', 'Sports')], default='FASHION', max_length=11),
        ),
        migrations.AddField(
            model_name='listing',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='listing',
            name='picture',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
