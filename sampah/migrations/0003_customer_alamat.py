# Generated by Django 5.0.2 on 2024-05-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sampah", "0002_invoice_alter_sampah_status_transactions"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="alamat",
            field=models.CharField(default=None, max_length=200),
        ),
    ]
