
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('productos/', include('gestion_productos.urls')),
    path('', include('gestion_productos.urls')),
]
