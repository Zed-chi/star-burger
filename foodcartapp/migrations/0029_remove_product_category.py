# Generated by Django 3.0.7 on 2020-06-29 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0028_auto_20200629_1024"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="category",
        ),
    ]
