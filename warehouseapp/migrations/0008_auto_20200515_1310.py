# Generated by Django 3.0.1 on 2020-05-15 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('warehouseapp', '0007_remove_damage_best_before'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damage',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_customer', to='warehouseapp.Customer'),
        ),
    ]
