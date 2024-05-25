from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField()


class Sampah(models.Model):
    tags = {"dry": "kering", "wet": "basah"}
    stats = {"WTG": "WAITING", "ACC": "ACCEPTED"}
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=200)
    jumlah = models.IntegerField()
    deskripsi = models.CharField(max_length=200)
    tag = models.CharField(max_length=6, choices=tags)
    status = models.CharField(max_length=8, choices=stats)
