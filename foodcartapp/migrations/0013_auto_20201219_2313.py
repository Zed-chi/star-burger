# Generated by Django 3.1.4 on 2020-12-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0012_order_payment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="comment",
            field=models.TextField(blank=True, default=""),
        ),
    ]
