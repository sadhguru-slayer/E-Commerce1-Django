# Generated by Django 4.0.4 on 2023-03-06 12:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerceapp', '0010_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_category', models.CharField(default='', max_length=20)),
                ('product_sub_category', models.CharField(default='', max_length=20)),
                ('product_desc', models.CharField(max_length=500)),
                ('product_price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to='images')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('stock', models.CharField(choices=[('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')], max_length=100)),
                ('Price_Filter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ecommerceapp.price_filter')),
                ('product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ecommerceapp.brands')),
                ('product_categore', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ecommerceapp.categories')),
            ],
        ),
    ]
