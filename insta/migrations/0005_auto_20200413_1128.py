# Generated by Django 3.0.4 on 2020-04-13 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20200413_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instauser',
            name='profilepic',
            field=models.ImageField(upload_to=''),
        ),
    ]
