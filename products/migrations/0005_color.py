# Generated by Django 4.1.5 on 2023-01-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_orders_rename_image_products_frontimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(null=True, upload_to='colors')),
                ('price', models.FloatField()),
            ],
        ),
    ]
