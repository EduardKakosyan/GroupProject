# Generated by Django 4.1.3 on 2023-05-17 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0013_remove_order_transaction_id_remove_order_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='order',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='account.order'),
        ),
    ]
