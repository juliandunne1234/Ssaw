# Generated by Django 3.2 on 2023-02-14 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20230211_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='product1',
            name='has_sizes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
