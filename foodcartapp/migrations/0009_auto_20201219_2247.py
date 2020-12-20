# Generated by Django 3.1.4 on 2020-12-19 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foodcartapp", "0008_auto_20201219_2230"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Handled", "Обработано"),
                    ("Unhandled", "Необработано"),
                ],
                default=("Handled", "Обработано"),
                max_length=125,
            ),
        ),
    ]
