# Generated by Django 5.1.1 on 2024-12-26 06:08

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_brand', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=50)),
                ('product_category', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price_inr', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('currency', models.CharField(max_length=30)),
                ('customer_review', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('available_sizes', models.CharField(max_length=100)),
                ('delivery_options', models.CharField(max_length=100)),
                ('additional_features', models.TextField()),
                ('expiration_date', models.DateField(auto_now=True)),
                ('packaging_type', models.CharField(max_length=50)),
                ('country_origin', models.CharField(max_length=50)),
                ('npk_content', models.CharField(max_length=50)),
                ('image_url', models.TextField(null=True)),
                ('details_slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='product_name', unique=True)),
            ],
        ),
    ]
