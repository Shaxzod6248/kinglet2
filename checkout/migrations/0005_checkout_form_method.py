# Generated by Django 4.1.5 on 2023-02-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_rename_dostavka_checkout_form_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout_form',
            name='method',
            field=models.CharField(choices=[('STANDARD', 'Standard'), ('EXPRESS', 'Express')], max_length=50, null=True),
        ),
    ]
