# Generated by Django 3.1.2 on 2020-10-06 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20201006_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='quuestions',
            name='s_n_o',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
