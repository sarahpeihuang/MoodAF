# Generated by Django 4.0.6 on 2023-05-07 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_patientdata_entrybox_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientdata',
            name='mood',
            field=models.CharField(blank=True, default='No mood', max_length=100),
        ),
    ]
