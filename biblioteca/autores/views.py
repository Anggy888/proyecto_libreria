from rest_framework import viewsets  # Importa la clase base 'viewsets' de Django REST Framework, que facilita la creación de vistas para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una API.

from .models import Autor  # Importa el modelo 'Autor' desde el archivo 'models.py' en el mismo directorio. Este modelo define la estructura de la tabla 'Autor' en la base de datos.

from .serializers import AutorSerializer  # Importa el serializer 'AutorSerializer' desde el archivo 'serializers.py'. Este serializer convierte las instancias de 'Autor' a formatos como JSON y viceversa.

class AutorViewSet(viewsets.ModelViewSet):  
    # Define una clase 'AutorViewSet' que hereda de 'viewsets.ModelViewSet'. 
    # 'ModelViewSet' es un conjunto de vistas predefinidas que Django REST Framework proporciona para manejar operaciones CRUD sobre un modelo.

    queryset = Autor.objects.all()  
    # Define la consulta (queryset) que esta vista manejará.
    # 'Autor.objects.all()' obtiene todos los objetos de la tabla 'Autor' en la base de datos. 
    # Este queryset se usará para listar, crear, actualizar o eliminar objetos 'Autor'.

    serializer_class = AutorSerializer  
    # Especifica que el serializer que se utilizará para convertir los objetos 'Autor' a JSON y viceversa es 'AutorSerializer'.
    # Este serializer se usa para la serialización de los datos cuando se realiza una operación CRUD en la API.
