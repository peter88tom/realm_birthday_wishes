# Generated by Django 4.0.3 on 2022-04-04 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirthdayTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('email_send', models.BooleanField(default=False)),
                ('email_send_year', models.IntegerField()),
                ('email_send_day', models.IntegerField()),
            ],
        ),
    ]