# Generated by Django 3.0.5 on 2022-01-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortHandle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
