# Generated by Django 2.0.4 on 2018-04-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze_visual', '0006_auto_20180428_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visual',
            name='image_url',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='visual',
            name='indicator',
            field=models.ManyToManyField(blank=True, null=True, to='data_scraping.Indicator'),
        ),
    ]
