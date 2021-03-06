# Generated by Django 3.0.5 on 2020-04-24 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0029_auto_20200423_1042'),
        ('build', '0011_auto_20200406_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='sales_order',
            field=models.ForeignKey(blank=True, help_text='SalesOrder to which this build is allocated', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='builds', to='order.SalesOrder'),
        ),
    ]
