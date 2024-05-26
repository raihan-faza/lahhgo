from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    alamat = models.CharField(max_length=200, default=None)

    def __str__(self) -> str:
        return self.user.first_name


class Sampah(models.Model):
    tags = {"dry": "kering", "wet": "basah"}
    stats = {"AVL": "AVAILABLE", "SLD": "SOLD"}
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=200)
    jumlah = models.IntegerField()
    deskripsi = models.CharField(max_length=200)
    tag = models.CharField(max_length=6, choices=tags)
    status = models.CharField(max_length=8, choices=stats)

    def __str__(self) -> str:
        return self.id


class Invoice(models.Model):
    total_harga = models.IntegerField()
    alamat_asal = models.CharField(max_length=200)
    alamat_tujuan = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.id


class Transactions(models.Model):
    transaction_invoice = models.OneToOneField(
        Invoice, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sampah = models.OneToOneField(Sampah, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.id


class InfoPenjemputan(models.Model):
    nama_kontak = models.CharField(max_length=200)
    no_kontak = models.CharField(max_length=200)
    kode_pos = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    detail_lokasi = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.customer.user.first_name
