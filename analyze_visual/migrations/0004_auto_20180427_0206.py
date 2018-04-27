# Generated by Django 2.0.4 on 2018-04-27 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_scraping', '0009_auto_20180426_0334'),
        ('analyze_visual', '0003_visual_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=140, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_scraping.State')),
            ],
        ),
        migrations.AlterField(
            model_name='visual',
            name='chart_type',
            field=models.CharField(choices=[('BAR', 'Bar Chart'), ('GEO', 'Geo Chart'), ('LINE', 'Line Chart'), ('PIE', 'Pie Chart')], default='GEO', max_length=32),
        ),
        migrations.AddField(
            model_name='stateinfo',
            name='visual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analyze_visual.Visual'),
        ),
    ]
