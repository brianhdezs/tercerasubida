from django.contrib import admin
from django.urls import path, include
from crud1.views import login,home, interfaz_sa

urlpatterns = [
    path('', home, name='home'),  # Redirecciona la ruta vacía al login
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),  # Asegúrate de tener esta línea también si la necesitas
    path('crud1/', include('crud1.urls')),
]
