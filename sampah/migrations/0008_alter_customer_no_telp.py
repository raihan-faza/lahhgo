# Generated by Django 5.0.3 on 2024-05-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampah', '0007_customer_no_telp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='no_telp',
            field=models.CharField(default=None, max_length=14),
        ),
    ]
