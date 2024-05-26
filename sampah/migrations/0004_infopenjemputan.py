# Generated by Django 5.0.6 on 2024-05-26 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sampah", "0003_customer_alamat"),
    ]

    operations = [
        migrations.CreateModel(
            name="InfoPenjemputan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nama_kontak", models.CharField(max_length=200)),
                ("no_kontak", models.CharField(max_length=200)),
                ("kode_pos", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("detail_lokasi", models.CharField(max_length=200)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sampah.customer",
                    ),
                ),
            ],
        ),
    ]