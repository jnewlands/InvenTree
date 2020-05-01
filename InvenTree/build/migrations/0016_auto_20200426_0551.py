# Generated by Django 3.0.5 on 2020-04-26 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0033_auto_20200426_0539'),
        ('build', '0015_auto_20200425_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='builditem',
            name='stock_item',
            field=models.ForeignKey(help_text='Stock Item to allocate to build', limit_choices_to={'belongs_to': None, 'build_order': None, 'customer': None}, on_delete=django.db.models.deletion.CASCADE, related_name='allocations', to='stock.StockItem'),
        ),
    ]