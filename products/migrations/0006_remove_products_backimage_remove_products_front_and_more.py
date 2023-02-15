# Generated by Django 4.1.5 on 2023-01-18 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='backimage',
        ),
        migrations.RemoveField(
            model_name='products',
            name='front',
        ),
        migrations.RemoveField(
            model_name='products',
            name='frontimage',
        ),
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title',
        ),
        migrations.AddField(
            model_name='orders',
            name='CardHolderName',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='CardNumber',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='backimage',
            field=models.ImageField(null=True, upload_to='cards1'),
        ),
        migrations.AddField(
            model_name='orders',
            name='frontimage',
            field=models.ImageField(null=True, upload_to='cards'),
        ),
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
        migrations.AlterField(
            model_name='color',
            name='price',
            field=models.TextField(),
        ),
    ]