from django import forms
from .models import Artikel, Program, KelolaGaleri

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul', 'isi', 'halaman', 'gambar']  # Pastikan field gambar dimasukkan

    gambar = forms.ImageField(required=False)  # Membuat field gambar tidak wajib

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['nama', 'deskripsi', 'gambar']

class KelolaGaleriForm(forms.ModelForm):
    class Meta:
        model = KelolaGaleri
        fields = ['foto', 'caption']
        widgets = {
            'caption': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan caption foto'}),
        }