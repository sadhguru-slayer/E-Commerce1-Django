# Generated by Django 4.0.4 on 2023-03-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerceapp', '0016_tag_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='producte',
            name='product_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
