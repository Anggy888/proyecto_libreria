"""
ASGI config for biblioteca project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os  # Importa el módulo os, que proporciona funciones para interactuar con el sistema operativo.

from django.core.asgi import get_asgi_application  # Importa la función get_asgi_application de Django, que configura la aplicación para que pueda ejecutarse como una aplicación ASGI.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca.settings')  
# Establece la variable de entorno DJANGO_SETTINGS_MODULE, que le indica a Django dónde encontrar el archivo de configuración.
# 'biblioteca.settings' es la ruta del archivo de configuración (settings.py) dentro del proyecto 'biblioteca'.
# Si esta variable ya está definida, no la cambia; solo la establece si no tiene valor.

application = get_asgi_application()  
# Llama a get_asgi_application() para obtener la aplicación ASGI de Django.
# ASGI (Asynchronous Server Gateway Interface) permite manejar peticiones asíncronas, como websockets, lo cual es útil para aplicaciones en tiempo real.
# Asigna la aplicación resultante a la variable application, que será utilizada por el servidor ASGI para ejecutar la aplicación Django.
