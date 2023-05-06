# Generated by Django 4.0.6 on 2023-05-06 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('entryBox', models.TextField(blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
