# Generated by Django 4.1.5 on 2023-01-30 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_checkout_form_dostavka'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout_form',
            old_name='dostavka',
            new_name='shipping',
        ),
    ]
