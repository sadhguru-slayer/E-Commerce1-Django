# Generated by Django 4.0.4 on 2023-03-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerceapp', '0018_alter_volume_filter_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.FloatField(default=0),
        ),
    ]