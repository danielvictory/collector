# Generated by Django 4.2 on 2023-04-26 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_schedule_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('profession', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='event',
            name='performers',
            field=models.ManyToManyField(to='main_app.performer'),
        ),
    ]