from django.contrib import admin
from django.urls import path, include
# ADICIONE ESTA LINHA ABAIXO:
from django.conf import settings 
# Se você estiver usando o static (para o debug_toolbar), adicione esta também:
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]

# A parte que está dando erro provavelmente é esta:
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns