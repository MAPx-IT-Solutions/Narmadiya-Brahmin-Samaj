# Generated by Django 2.2.4 on 2020-05-23 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Narmadiya', '0011_auto_20200523_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='heading',
            field=models.CharField(default='suhdjsdngjl', max_length=100, verbose_name='Heading'),
        ),
    ]
