# Generated by Django 2.2.4 on 2020-05-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Narmadiya', '0010_auto_20200523_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(default='settings.MEDIA_ROOT/News/Images/galactic_interstellar_5k.jpg', upload_to='News/Images', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(default='News/Video/default.mp4', upload_to='News/Video', verbose_name='Video'),
        ),
    ]
