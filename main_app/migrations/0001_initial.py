# Generated by Django 4.2 on 2023-04-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('classifier', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=300)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
