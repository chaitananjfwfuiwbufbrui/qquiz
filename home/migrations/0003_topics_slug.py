# Generated by Django 3.1.2 on 2020-10-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_quuestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='slug',
            field=models.SlugField(default='fcdfd', max_length=40),
        ),
    ]