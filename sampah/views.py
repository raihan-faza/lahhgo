from django.shortcuts import render
from .models import (
    Customer,
    Sampah,
    Invoice,
    Transactions
)
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import (
    require_POST,
    require_GET
)
from django.core.serializers import serialize


def index_sampah(request):
    kumpulan_sampah = Sampah.objects.filter(status="AVL")
    kumpulan_sampah = serialize('json', kumpulan_sampah)
    return JsonResponse(
        {
            "kumpulan_sampah": kumpulan_sampah
        }
    )


@require_POST
def create_sampah(request):
    try:
        jenis = request.POST.get("jenis")
        jumlah = request.POST.get("jumlah")
        deskripsi = request.POST.get("deskripsi")
        tag = request.POST.get("tag")
        status = request.POST.get("status")
        user = User.object.filter(id=request.user.id)
        sampah = Sampah(user=user, jenis=jenis, jumlah=jumlah,
                        deskripsi=deskripsi, tag=tag, status=status)
        sampah.save()
    except:
        return JsonResponse(
            {
                "message": "sampah post failed"
            }
        )
    return JsonResponse(
        {
            "message": f"{sampah.user} succesfully post sampah"
        }
    )


@require_POST
def update_sampah(request):
    try:
        id_sampah = request.POST.get("id_sampah")
        jumlah = request.POST.get("jumlah")
        deskripsi = request.POST.get("deskripsi")
        tag = request.POST.get("tag")
        sampah = Sampah.objects.filter(id=id_sampah)
        sampah.update(jumlah=jumlah, deskripsi=deskripsi, tag=tag)
    except:
        return JsonResponse(
            {
                "message": "update failed"
            }
        )
    return JsonResponse(
        {
            "message": "update succesfull"

        }
    )


@require_POST
def delete_sampah(request):
    try:
        id_sampah = request.POST.get("id_sampah")
        sampah = Sampah.objects.filter(id=id_sampah)
        sampah.delete()
    except:
        return JsonResponse(
            {
                "message": "deletion failed"
            }
        )
    return JsonResponse(
        {
            "message": "sampah succesfully deleted"
        }
    )


@require_GET
def show_sampah(request):
    id_sampah = request.GET.get("id_sampah")
    try:
        sampah = Sampah.objects.filter(id=id_sampah)
    except:
        return JsonResponse(
            {
                "message": "failed to fetch data"
            }
        )
    return JsonResponse(
        {
            "sampah": sampah
        }
    )


def generate_point(jumlah_sampah):
    # jumlah sampah dalam satuan kg
    return jumlah_sampah * 100

@require_POST
def create_transction(request):
    id_sampah = request.POST.get("id_sampah")
    try:
        user = User.objects.filter(id=request.user.id)
        buyer = Customer.objects.filter(user=user)
        sampah = Sampah.objects.filter(id=id_sampah)
        seller = Customer.objects.filter(user=sampah.user)
        invoice = Invoice(sampah=sampah, alamat_asal=seller.alamat,
                          alamat_tujuan=buyer.alamat)
        sampah.status = "SLD"
        invoice.save()
        transaction = Transactions(
            invoice=invoice, customer=buyer, sampah=sampah)
        transaction.save()
        points = generate_point(sampah.jumlah)
        seller.points = seller.points + points
    except:
        return JsonResponse(
            {
                "message": "transaction failed"
            }
        )
    return JsonResponse(
        {
            "message": "transaction success",
            "buyer": f"{buyer.name}",
            "seller": f"{seller.name}",
            "sampah": {
                "jenis": f"{sampah.jenis}",
                "jumlah": f"{sampah.jumlah}"
            }
        }
    )
