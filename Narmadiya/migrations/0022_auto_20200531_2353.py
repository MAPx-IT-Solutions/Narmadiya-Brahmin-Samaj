# Generated by Django 2.2.4 on 2020-05-31 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Narmadiya', '0021_auto_20200531_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimony',
            name='altmobileno',
            field=models.BigIntegerField(default=0, verbose_name=' Alternate Mobile Number'),
        ),
    ]
