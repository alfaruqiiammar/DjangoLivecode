from django import forms

from .models import Barang


class BarangForm(forms.ModelForm):
    """Form definition for Blog."""

    class Meta:
        """Meta definition for Blogform."""

        model = Barang
        fields = ('foto', 'nama', 'harga', 'deskripsi')