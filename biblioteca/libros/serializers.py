from rest_framework import serializers  # Importa el módulo serializers de Django REST Framework para crear serializadores.
from .models import Libro  # Importa el modelo Libro desde el módulo actual.
from autores.models import Autor  # Importa el modelo Autor desde la aplicación autores.
from autores.serializers import AutorSerializer  # Importa el serializador AutorSerializer para manejar la serialización de autores.

class LibroSerializer(serializers.ModelSerializer):
    # Define el serializador para el modelo Libro, heredando de ModelSerializer para simplificar la creación de serializadores.

    autor = AutorSerializer()  # Define un campo 'autor' que usará el serializador AutorSerializer para serializar y deserializar datos del autor.

    class Meta:
        model = Libro  # Indica que este serializador está asociado al modelo Libro.
        fields = ['id', 'titulo', 'autor', 'fecha_publicacion', 'resumen']  # Define los campos que se incluirán en la serialización.

    def create(self, validated_data):
        # Método para crear una nueva instancia del modelo Libro.

        autor_data = validated_data.pop('autor')  # Extrae los datos del autor del diccionario de datos validados.
        # pop() elimina 'autor' del diccionario y lo retorna para que se pueda usar en la creación del autor.

        autor, created = Autor.objects.get_or_create(**autor_data)  # Busca el autor en la base de datos o lo crea si no existe.
        # get_or_create() retorna una tupla: el objeto autor y un booleano que indica si fue creado o no.

        libro = Libro.objects.create(autor=autor, **validated_data)  # Crea una nueva instancia de Libro utilizando el autor obtenido y los datos validados.
        return libro  # Retorna la instancia del libro creado.
