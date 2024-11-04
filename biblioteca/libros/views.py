from rest_framework import viewsets  # Importa el módulo viewsets de Django REST Framework para crear conjuntos de vistas basadas en modelos.
from .models import Libro  # Importa el modelo Libro desde el módulo actual.
from .serializers import LibroSerializer  # Importa el serializador LibroSerializer para manejar la serialización de libros.

class LibroViewSet(viewsets.ModelViewSet):
    # Define un conjunto de vistas para el modelo Libro, que proporciona acciones CRUD (Crear, Leer, Actualizar, Borrar) automáticamente.

    queryset = Libro.objects.all()  # Establece la consulta que se utilizará para recuperar objetos Libro. Aquí se obtienen todos los libros en la base de datos.

    serializer_class = LibroSerializer  # Especifica el serializador que se utilizará para convertir los datos del modelo Libro a y desde JSON.
