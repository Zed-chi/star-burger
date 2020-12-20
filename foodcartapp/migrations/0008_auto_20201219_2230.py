# Generated by Django 3.1.4 on 2020-12-19 19:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0007_remove_order_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="registered_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
