# Generated by Django 5.1.5 on 2025-01-31 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_rental'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='images',
        ),
        migrations.AddField(
            model_name='rental',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='rentals/'),
        ),
        migrations.AlterField(
            model_name='rental',
            name='owner_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental',
            name='property_type',
            field=models.CharField(max_length=50),
        ),
    ]
