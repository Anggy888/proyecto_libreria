from django.db import models  # Importa el módulo models de Django, que contiene clases base para definir modelos en la base de datos


class Autor(models.Model):  # Define una clase llamada Autor, que hereda de models.Model y representa una tabla en la base de datos
    nombre = models.CharField(max_length=100)  
    # Define un campo de tipo CharField, que almacena texto de longitud fija o variable.
    # max_length=100 limita el campo a 100 caracteres. Aquí, 'nombre' almacenará el nombre del autor.

    nacionalidad = models.CharField(max_length=100)  
    # Otro campo de tipo CharField, limitado a 100 caracteres.
    # 'nacionalidad' guardará la nacionalidad del autor.

    fecha_nacimiento = models.DateField()  
    # Define un campo de tipo DateField para almacenar fechas.
    # Este campo almacenará la fecha de nacimiento del autor.

    def __str__(self):  
        # Define el método especial __str__, que especifica la representación en texto del objeto Autor.
        # Este método es útil para mostrar el nombre del autor en el panel de administración y otros contextos.

        return self.nombre  
        # Devuelve el valor del campo 'nombre' cuando se convierte un objeto Autor a una cadena.
        # Esto hace que en el panel de administración de Django se muestre el nombre del autor en lugar de un valor numérico o abstracto.
