# Generated by Django 5.1 on 2024-08-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_alter_listing_photo_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.ImageField(default='default_photos/default_no_photo.jpg', upload_to='images/%Y/%m/%d/'),
        ),
    ]
