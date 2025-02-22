# Generated by Django 3.0.4 on 2020-04-12 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('caption', models.CharField(blank=True, max_length=256, null=True)),
                ('likes', models.PositiveIntegerField()),
                ('owner', models.CharField(max_length=200)),
                ('date_uploaded', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='instauser',
            name='followers',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='instauser',
            name='following',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
