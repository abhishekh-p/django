# Generated by Django 5.1.1 on 2024-11-01 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0021_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='uss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
