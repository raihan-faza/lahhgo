from django.shortcuts import render
from .models import (
    Customer,
    Sampah
)
from django.contrib.auth.models import User
from django.http import JsonResponse


def index_sampah(request):
    kumpulan_sampah = Sampah.objects.all()
    return JsonResponse({"kumpulan_sampah": kumpulan_sampah})


def create_sampah(request):
    try:
        user = User.object.get(id=request.user.id)
        jenis = request.POST.get("jenis")
        jumlah = request.POST.get("jumlah")
        deskripsi = request.POST.get("deskripsi")
        tag = request.POST.get("tag")
        status = request.POST.get("status")
        sampah = Sampah(user=user, jenis=jenis, jumlah=jumlah,
                        deskripsi=deskripsi, tag=tag, status=status)
        sampah.save()
    except:
        return JsonResponse({"message": "sampah post failed"})
    return JsonResponse({"message": f"{sampah.user} succesfully post sampah"})


def update_sampah(request):
    id_sampah = request.POST.get("id_sampah")
    jumlah = request.POST.get("jumlah")
    deskripsi = request.POST.get("deskripsi")
    tag = request.POST.get("tag")
    sampah = Sampah.objects.filter(id=id_sampah)
    sampah.update(jumlah=jumlah, deskripsi=deskripsi, tag=tag)


def delete_sampah(request):
    id_sampah = request.POST.get("id_sampah")
    sampah = Sampah.objects.filter(id=id_sampah)
    sampah.delete()


def show_sampah(request):
    id_sampah = request.POST.get("id_sampah")
    sampah = Sampah.objects.filter(id=id_sampah)
    return JsonResponse({"sampah": sampah})


def beli_sampah(request):
    # ini belom ya, aku blom tau harga sampahnya
    user = User.object.get(id=request.user.id)
    id_sampah = request.POST.get("id_sampah")
    sampah = Sampah.objects.filter(id=id_sampah)
    customer = Customer.objects.filter(user=user)
    sampah.update(status="ACC")
    # customer.point =
    return


def add_point(customer, sampah):
    return
