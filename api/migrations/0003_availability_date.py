# Generated by Django 4.2.1 on 2023-06-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_availability_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='availability',
            name='date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date'),
        ),
    ]
