# Generated by Django 3.0.4 on 2020-04-14 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0007_photo_owner_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='owner_profilepic',
            field=models.ImageField(upload_to=''),
        ),
    ]
