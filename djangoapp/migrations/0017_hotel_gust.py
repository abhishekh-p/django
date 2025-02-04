# Generated by Django 5.1.1 on 2024-10-28 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0016_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=15)),
                ('rate', models.FloatField()),
                ('decsription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gust_name', models.CharField(max_length=15)),
                ('check_in', models.DateField()),
                ('hotels', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.hotel')),
            ],
        ),
    ]
