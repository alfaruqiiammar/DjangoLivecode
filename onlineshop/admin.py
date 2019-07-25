from django.contrib import admin

# Register your models here.
from .models import Barang

class BarangAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'harga']  
    list_display_links = ['nama']

admin.site.register(Barang, BarangAdmin)