# Generated by Django 3.1.2 on 2020-10-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_topics_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='slug',
            field=models.SlugField(max_length=40),
        ),
    ]
