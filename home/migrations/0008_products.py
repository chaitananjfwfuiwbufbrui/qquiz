# Generated by Django 3.1.2 on 2020-10-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('prize', models.IntegerField(default=0)),
                ('category', models.CharField(default='', max_length=50)),
                ('sub_category', models.CharField(default='', max_length=50)),
                ('product_image', models.ImageField(default='', upload_to='shop/images')),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]