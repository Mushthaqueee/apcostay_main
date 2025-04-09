# Generated by Django 5.1.5 on 2025-02-01 05:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_remove_rental_image_rentalimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='email',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='owner_name',
        ),
        migrations.RemoveField(
            model_name='rental',
            name='phone',
        ),
        migrations.AddField(
            model_name='rental',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='listings.registerdb'),
            preserve_default=False,
        ),
    ]
