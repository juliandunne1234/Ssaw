# Generated by Django 3.2 on 2023-02-14 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product1_has_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product1',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
