# Generated by Django 3.1.4 on 2020-12-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0005_order_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            field=models.DateTimeField(auto_now_add=True),
            name="registered_at",
        ),
        migrations.AddField(
            model_name="order",
            name="called_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="delivered_at",
            field=models.DateTimeField(null=True),
        ),
    ]
