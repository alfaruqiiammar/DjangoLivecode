from django.shortcuts import render
from .models import Barang
from .forms import BarangForm
# Create your views here.


def katalogBarang(request):
    barang = Barang.objects.all()
    return render(request, 'home.html', {'barangs': barang})

def barang_detail(request, barang_id):
    try:
        barang = Barang.objects.get(pk=barang_id)
    except Barang.DoesNotExist:
        raise Http404('Barang does not exist')
    return render(request, 'barang_detail.html', {'barang': barang})


def input_barang(request):
    if request.method == "POST":
        form = BarangForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
    else:
        form = BarangForm()
    return render(request, 'input_barang.html', {'formBarang': form})