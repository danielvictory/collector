# Generated by Django 4.2 on 2023-04-26 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_schedule_delete_adddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(verbose_name='Schedule Date'),
        ),
    ]
