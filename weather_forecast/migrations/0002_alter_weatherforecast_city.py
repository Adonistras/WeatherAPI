# Generated by Django 4.1 on 2022-08-26 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city', '0001_initial'),
        ('weather_forecast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherforecast',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weather_forecast', to='city.city', verbose_name='City_id'),
        ),
    ]
