# Generated by Django 2.2.4 on 2020-05-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Narmadiya', '0015_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='content',
            field=models.ImageField(default='', upload_to='Adv/Images', verbose_name='File'),
        ),
    ]
