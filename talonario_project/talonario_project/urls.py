from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from registros.views import CustomLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),
    
    # Autenticación
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),

    # Aplicación principal
    path('registros/', include('registros.urls')),

    # Redirección inicial
    path('', lambda request: redirect('login'), name='home'),
]

# Configuración para servir archivos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
