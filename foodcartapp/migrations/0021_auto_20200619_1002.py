# Generated by Django 3.0.7 on 2020-06-19 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0020_auto_20200619_0959"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="order_type",
            new_name="payment_type",
        ),
    ]