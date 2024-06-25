from django.shortcuts import redirect, render
from .models import (
    Customer,
    Sampah,
    Invoice,
    Transactions
)
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.http import (
    require_POST,
    require_GET
)
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login as auth_login


def index_sampah(request):
    # kumpulan_sampah = Sampah.objects.filter(status="AVAILABLE")
    # kumpulan_sampah = serialize('json', kumpulan_sampah)
    return render(request, "index.html")



@require_POST
def create_sampah(request):
    try:
        jenis = request.POST.get("jenis")
        jumlah = request.POST.get("jumlah")
        deskripsi = request.POST.get("deskripsi")
        tag = request.POST.get("tag")
        status = request.POST.get("status")
        image_name = request.POST.get("file_name") or None
        uploaded_image = request.FILES.get(image_name) or None
        user = User.object.filter(id=request.user.id)
        sampah = Sampah(user=user, jenis=jenis, jumlah=jumlah,
                        deskripsi=deskripsi, tag=tag, status=status, foto_sampah=uploaded_image)
        sampah.save()
        with open(f"images/{image_name}", "wb") as loc:
            for chunk in uploaded_image.chunks():
                loc.write(chunk)
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


def show_products(request):
    return render(request, "products.html", {})


def generate_point(jumlah_sampah):
    # jumlah sampah dalam satuan kg
    return jumlah_sampah * 100


@require_POST
def create_transaction(request):
    id_sampah = request.POST.get("id_sampah")
    sampah = Sampah.objects.filter(id=id_sampah)
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


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login Success")
            return redirect("/shop/")
        else:
            messages.error(request, "Login Failed")
            return redirect("/shop/login")
    return render(request, "login.html", {'action_url': '/shop/login/'})


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Username or email already exists")
            return redirect("/shop/register")
        user = User.objects.create_user(
            username=username, password=password, email=email)
        customer = Customer(user=user, points=0, alamat="")
        user.save()
        customer.save()
        return redirect("/shop/login")
    return render(request, "register.html", {'action_url': '/shop/register/'})


def edit_profile(request):
    new_alamat = request.POST.get("new_alamat")
    new_email = request.POST.get("new_email")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    no_telp = request.POST.get("no_telp")
    user = User.objects.filter(id=request.user.id)
    customer = Customer.objects.filter(user=user)
    user.update(first_name=first_name, last_name=last_name)
    customer.update(alamat=new_alamat, email=new_email, no_telp=no_telp)
    return


def upload3(request):
    return render(request, "upload3.html")

def how_it_works(request):
    return render(request, "how-it-works.html")