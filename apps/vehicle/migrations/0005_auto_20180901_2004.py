# Generated by Django 2.1 on 2018-09-02 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20180901_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(default='/photos_cars/photo_car_default.png', upload_to='photos_cars/%d'),
        ),
    ]
