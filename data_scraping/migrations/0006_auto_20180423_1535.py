# Generated by Django 2.0.4 on 2018-04-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_scraping', '0005_auto_20180423_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countypop',
            name='population',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
