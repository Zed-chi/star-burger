# Generated by Django 3.1.4 on 2020-12-19 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0004_auto_20201219_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default=''),
        ),
    ]