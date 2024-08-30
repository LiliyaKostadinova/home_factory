# Generated by Django 5.1 on 2024-08-30 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_listing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('for rent', 'For Rent'), ('for sale', 'For Sale')], max_length=20),
        ),
    ]
