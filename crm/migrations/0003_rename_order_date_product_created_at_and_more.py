# Generated by Django 4.2.23 on 2025-06-29 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_rename_created_at_product_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='order_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
