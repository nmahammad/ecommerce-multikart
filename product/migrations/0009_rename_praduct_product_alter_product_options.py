# Generated by Django 4.0.3 on 2022-03-11 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_productversion'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Praduct',
            new_name='Product',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Product'},
        ),
    ]
