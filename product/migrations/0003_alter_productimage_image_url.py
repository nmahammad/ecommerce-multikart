# Generated by Django 4.0.3 on 2022-04-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productimage_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image_url',
            field=models.ImageField(upload_to='media/categories/'),
        ),
    ]
