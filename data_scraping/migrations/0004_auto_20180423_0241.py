# Generated by Django 2.0.4 on 2018-04-23 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_scraping', '0003_auto_20180423_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='year',
            field=models.CharField(max_length=4),
        ),
    ]
