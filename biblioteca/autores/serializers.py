from rest_framework import serializers
from .models import Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad', 'fecha_nacimiento']
