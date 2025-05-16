from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from .models import Artikel, Program, KelolaGaleri
from .forms import ArtikelForm, ProgramForm, KelolaGaleriForm
from django.shortcuts import render
from .models import Artikel, KelolaGaleri  # pastikan kamu mengimpor model galeri
# Halaman utama (home)

def home(request):
    # Ambil artikel untuk halaman home
    artikel_list = Artikel.objects.filter(halaman='home')
    
    # Ambil artikel untuk halaman tentang
    artikel_tentang = Artikel.objects.filter(halaman='tentang').order_by('-tanggal')
    
    # Ambil daftar program untuk halaman program
    program_list = Program.objects.all()
    
    # Ambil galeri jika ada (untuk halaman tentang)
    galeri = KelolaGaleri.objects.all().order_by('-id')
    
    # Gabungkan semua data dalam satu context
    context = {
        'artikel_list': artikel_list,
        'artikel_tentang': artikel_tentang,
        'program_list': program_list,
        'galeri': galeri,
    }

    return render(request, 'profil/home.html', context)

# Halaman Dashboard Admin
@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'profil/dashboard.html')

# View untuk login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'profil/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# Kelola Artikel (diperbaiki untuk menangani upload gambar)
@login_required
def kelola_artikel(request):
    if not request.user.is_staff:
        return redirect('home')

    artikel_list = Artikel.objects.all().order_by('-tanggal')

    if request.method == 'POST':
        form = ArtikelForm(request.POST, request.FILES)  # ✅ Perbaikan di sini
        if form.is_valid():
            form.save()
            return redirect('kelola_artikel')
    else:
        form = ArtikelForm()

    return render(request, 'profil/kelola_artikel.html', {
        'form': form,
        'artikel_list': artikel_list
    })

@login_required
def hapus_artikel(request, id):
    if not request.user.is_staff:
        return redirect('home')

    artikel = get_object_or_404(Artikel, id=id)
    artikel.delete()
    return redirect('kelola_artikel')

@login_required
def detail_artikel(request, slug):
    artikel = get_object_or_404(Artikel, slug=slug)
    return render(request, 'profil/detail_artikel.html', {'artikel': artikel})

@login_required
def kelola_program(request):
    program_list = Program.objects.all()
    
    # Jika form dikirim
    if request.method == 'POST':
        form = ProgramForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kelola_program')
    else:
        form = ProgramForm()
    
    return render(request, 'profil/kelola_program.html', {
        'form': form,
        'program_list': program_list
    })

@login_required
def hapus_program(request, id):
    program = get_object_or_404(Program, id=id)
    program.delete()
    return redirect('kelola_program')

@login_required
def kelola_galeri_view(request):
    if request.method == 'POST':
        form = KelolaGaleriForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('kelola_galeri')  # Pastikan URL name sesuai
    else:
        form = KelolaGaleriForm()

    galeri = KelolaGaleri.objects.all().order_by('-id')  # menampilkan terbaru dulu
    context = {
        'form': form,
        'galeri': galeri,
    }
    return render(request, 'profil/kelola_galeri.html', context)

def hapus_foto(request, foto_id):
    foto = get_object_or_404(KelolaGaleri, id=foto_id)
    foto.delete()
    return redirect('kelola_galeri') 