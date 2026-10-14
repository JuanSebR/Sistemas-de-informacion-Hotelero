from django.contrib import admin
from django.urls import path, include
from usuarios.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('usuarios/', include('usuarios.urls')),
    path('', include('usuarios.urls')),
]
