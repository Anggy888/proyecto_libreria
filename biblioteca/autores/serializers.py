from rest_framework import serializers  # Importa el módulo serializers de Django REST framework, que permite convertir instancias de modelos a formatos como JSON para APIs.

from .models import Autor  # Importa el modelo Autor desde el archivo models en el mismo directorio. Este modelo representa la estructura de los datos de un autor en la base de datos.

class AutorSerializer(serializers.ModelSerializer):  
    # Define una clase AutorSerializer que hereda de serializers.ModelSerializer.
    # ModelSerializer es una clase de atajo que automáticamente genera un serializer basado en el modelo especificado.

    class Meta:  # Meta es una clase interna utilizada para especificar opciones de configuración.
        model = Autor  # Especifica que este serializer se basa en el modelo Autor.
        
        fields = ['id', 'nombre', 'nacionalidad', 'fecha_nacimiento']  
        # Define los campos del modelo Autor que se incluirán en el serializer.
        # En este caso, se incluyen 'id', 'nombre', 'nacionalidad', y 'fecha_nacimiento'.
        # Estos campos serán convertidos a formato JSON (u otros) cuando se utilice el serializer.
