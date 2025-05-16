from django.contrib import admin
from .models import Artikel, Program, KelolaGaleri

@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul', 'halaman', 'tanggal')
    list_filter = ('halaman', 'tanggal')
    search_fields = ('judul', 'isi')
    prepopulated_fields = {'slug': ('judul',)}
    ordering = ['-tanggal']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    search_fields = ('nama', 'deskripsi')

@admin.register(KelolaGaleri)
class KelolaGaleriAdmin(admin.ModelAdmin):
    list_display = ('caption',)
    search_fields = ('caption',)
