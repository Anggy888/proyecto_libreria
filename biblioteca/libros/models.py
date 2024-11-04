from django.db import models  # Importa el módulo models desde django.db, que contiene las clases y funciones para definir modelos de base de datos.
from autores.models import Autor  # Importa el modelo Autor desde la aplicación autores. Esto permite crear una relación entre Libro y Autor.

class Libro(models.Model):
    # Define la clase Libro que hereda de models.Model. Esto convierte a Libro en un modelo de base de datos de Django.
    
    titulo = models.CharField(max_length=200)  
    # Define un campo 'titulo' que almacenará texto. 
    # CharField se usa para cadenas de texto cortas, y max_length establece el límite de caracteres en 200.

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')  
    # Define un campo 'autor' que establece una relación de clave foránea con el modelo Autor.
    # Esto significa que cada libro tiene un autor asociado.
    # on_delete=models.CASCADE indica que si un autor es eliminado, también se eliminarán los libros relacionados.
    # related_name='libros' permite acceder a todos los libros de un autor usando autor.libros.all().

    fecha_publicacion = models.DateField()  
    # Define un campo 'fecha_publicacion' que almacenará la fecha de publicación del libro.
    # DateField se usa para almacenar fechas.

    resumen = models.TextField()  
    # Define un campo 'resumen' que almacenará un texto más largo, como un resumen del libro.
    # TextField se utiliza para cadenas de texto largas.

    def __str__(self):
        # Define el método __str__ que retorna el título del libro cuando se imprime una instancia de este modelo.
        return self.titulo
