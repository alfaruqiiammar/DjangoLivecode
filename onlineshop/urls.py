from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.katalogBarang, name='home'),
    path('barang/<int:barang_id>/', views.barang_detail, name='barang_detail'),
    path('barang/tambah/', views.input_barang, name='inputbarang'),
]