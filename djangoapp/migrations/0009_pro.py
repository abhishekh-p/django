# Generated by Django 5.1.1 on 2024-10-16 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_admn'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro',
            fields=[
                ('pro_id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_name', models.CharField(max_length=100)),
                ('use1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.product')),
            ],
        ),
    ]
