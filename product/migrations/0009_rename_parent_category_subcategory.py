# Generated by Django 4.0.3 on 2022-04-22 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_rename_subcategory_category_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='parent',
            new_name='subcategory',
        ),
    ]
