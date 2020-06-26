# Generated by Django 2.2.4 on 2020-05-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(default='', max_length=100, verbose_name='Heading')),
                ('news', models.CharField(default='', max_length=500, verbose_name='News')),
                ('images', models.ImageField(upload_to='News/Images', verbose_name='Image')),
                ('video', models.FileField(upload_to='News/Video', verbose_name='Video')),
            ],
        ),
    ]