# Generated by Django 4.1.5 on 2023-01-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout_form',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='checkout_form',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='checkout_form',
            name='country',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='checkout_form',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='checkout_form',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='checkout_form',
            name='postal',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='checkout_form',
            name='state',
            field=models.CharField(max_length=70, null=True),
        ),
    ]