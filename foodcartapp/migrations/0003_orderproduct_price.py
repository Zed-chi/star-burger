# Generated by Django 3.1.4 on 2020-12-18 13:40

from django.db import migrations, models

def set_price_to_ordered_products(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    OrderProduct = apps.get_model('foodcartapp', 'OrderProduct')
    for item in OrderProduct.objects.all():
        item.name = item.product.price
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0002_auto_20201214_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.RunPython(set_price_to_ordered_products)
    ]