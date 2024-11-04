from django.apps import AppConfig  # Importa la clase AppConfig desde el módulo django.apps

class LibrosConfig(AppConfig):  
    # Define una clase `LibrosConfig` que hereda de `AppConfig`. Esta clase configura la aplicación 'libros'.
    
    default_auto_field = 'django.db.models.BigAutoField'  
    # Establece el tipo de campo que se utilizará para los identificadores automáticos (ID).
    # En este caso, se utiliza 'BigAutoField', que permite un rango mayor de identificadores.
    
    name = 'libros'  
    # Define el nombre de la aplicación como 'libros'.
    # Este nombre se utilizará en la configuración del proyecto para referirse a esta aplicación.
