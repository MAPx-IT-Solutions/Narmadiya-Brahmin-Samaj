# Generated by Django 2.2.4 on 2020-05-31 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Narmadiya', '0020_auto_20200531_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimony',
            name='photo',
            field=models.FileField(default='', max_length=30, upload_to='Matrimony/Images', verbose_name='Photo'),
        ),
    ]
