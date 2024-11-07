# Generated by Django 5.1.1 on 2024-10-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0005_crud'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='crud',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='crud',
            name='phone_number',
            field=models.IntegerField(max_length=10),
        ),
    ]
