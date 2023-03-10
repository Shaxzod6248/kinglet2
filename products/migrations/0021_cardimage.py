# Generated by Django 4.1.5 on 2023-02-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_products_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cardimage')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
