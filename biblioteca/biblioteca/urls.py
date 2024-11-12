"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Importa el módulo admin de Django para habilitar el panel de administración del proyecto.

from django.urls import path, include  # Importa path para definir rutas de URL y include para incluir conjuntos de URLs de otras aplicaciones.

from rest_framework.routers import DefaultRouter  # Importa DefaultRouter de Django REST framework, el cual ayuda a generar automáticamente rutas de URL para los ViewSets.

from autores.views import AutorViewSet  # Importa el ViewSet AutorViewSet desde el archivo views de la aplicación autores.
from libros.views import LibroViewSet  # Importa el ViewSet LibroViewSet desde el archivo views de la aplicación libros.

router = DefaultRouter()  # Crea una instancia de DefaultRouter, que será usada para registrar los ViewSets y crear automáticamente las rutas de la API.

router.register(r'autores', AutorViewSet)  
# Registra el AutorViewSet en el enrutador con el prefijo 'autores'.
# Esto generará automáticamente las rutas CRUD (listar, crear, actualizar y eliminar) para los autores en la API.
#la r asegura que cualquier carácter dentro de la cadena sea interpretado literalmente.

router.register(r'libros', LibroViewSet)  
# Registra el LibroViewSet en el enrutador con el prefijo 'libros'.
# Esto generará automáticamente las rutas CRUD para los libros en la API.

urlpatterns = [
    path('admin/', admin.site.urls),  
    # Define la ruta para el panel de administración de Django, accesible en /admin/.

    path('api/', include(router.urls)),  
    # Incluye las URLs generadas automáticamente por el enrutador (router).
    # Con el prefijo 'api/', todas las rutas registradas por el enrutador (para autores y libros) estarán accesibles bajo '/api/'.
]

