# Generated by Django 3.2 on 2023-02-11 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='select_size',
        ),
    ]
