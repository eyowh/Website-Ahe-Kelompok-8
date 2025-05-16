from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import logout_view, kelola_galeri_view, hapus_foto

urlpatterns = [
    path('', views.home, name='home'),  # Beranda atau halaman utama
    path('tentang/home', views.home, name='tentang'),  # Tentang tetap mengarah ke home
    path('program/home', views.home, name='program'),  # Program tetap mengarah ke home
    path('kontak/home', views.home, name='kontak'),
    path('login/', auth_views.LoginView.as_view(template_name='profil/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/kelola-artikel/', views.kelola_artikel, name='kelola_artikel'),
    path('dashboard/hapus-artikel/<int:id>/', views.hapus_artikel, name='hapus_artikel'),

    # ✅ Tambahkan ini untuk detail artikel berdasarkan slug
    path('artikel/<slug:slug>/', views.detail_artikel, name='detail_artikel'),
    path('dashboard/kelola-program/', views.kelola_program, name='kelola_program'),
    path('dashboard/hapus-program/<int:id>/', views.hapus_program, name='hapus_program'),
    path('dashboard/kelola_galeri/', kelola_galeri_view, name='kelola_galeri'),
    path('dashboard/kelola_galeri/hapus/<int:foto_id>/', hapus_foto, name='hapus_foto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
