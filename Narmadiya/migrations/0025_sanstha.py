# Generated by Django 2.2.4 on 2020-06-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Narmadiya', '0024_dandakshina_sampark'),
    ]

    operations = [
        migrations.CreateModel(
            name='sanstha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Sanstha/img', verbose_name='Image')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Name of Sanstha')),
                ('description', models.CharField(default='', max_length=500, verbose_name='Description of Sanstha')),
                ('xcoordinate', models.IntegerField(default=0, verbose_name='x-Coordiname')),
                ('ycoordinate', models.IntegerField(default=0, verbose_name='y-Coordiname')),
            ],
        ),
    ]