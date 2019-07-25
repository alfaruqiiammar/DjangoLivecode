from django.db import models

# Create your models here.

class Barang(models.Model):
    foto = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)
    harga = models.CharField(max_length=100)
    deskripsi = models.TextField()
