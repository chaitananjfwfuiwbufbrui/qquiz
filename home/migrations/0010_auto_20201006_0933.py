# Generated by Django 3.1.2 on 2020-10-06 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201006_0931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quuestions',
            name='s_no',
        ),
        migrations.AddField(
            model_name='quuestions',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
