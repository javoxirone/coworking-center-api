# Generated by Django 4.2.1 on 2023-06-05 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_availability_is_available_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name of the resident'),
        ),
    ]
