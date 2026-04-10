from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Importante para verificar o DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('products.urls')),
]

# Adicione este bloco abaixo para registrar o Debug Toolbar apenas em modo DEBUG
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns