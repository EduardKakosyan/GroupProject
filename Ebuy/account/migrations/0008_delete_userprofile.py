# Generated by Django 4.1.3 on 2023-05-15 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_customer_order_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
