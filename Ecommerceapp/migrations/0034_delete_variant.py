# Generated by Django 4.0.4 on 2023-05-08 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerceapp', '0033_remove_product_volume_filter_remove_variant_volume_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Variant',
        ),
    ]
