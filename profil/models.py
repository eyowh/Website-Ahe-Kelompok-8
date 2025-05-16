from django.db import models
from django.utils.text import slugify

class Artikel(models.Model):
    JENIS_HALAMAN = [
        ('home', 'Home'),
        ('tentang', 'Tentang Kami'),
    ]

    judul = models.CharField(max_length=200)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    halaman = models.CharField(max_length=20, choices=JENIS_HALAMAN)
    gambar = models.ImageField(upload_to='artikel/', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul

class Program(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='program/', null=True, blank=True)

    def __str__(self):
        return self.nama
    
class KelolaGaleri(models.Model):
    foto = models.ImageField(upload_to='galeri/')
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption