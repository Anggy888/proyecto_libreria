from django.apps import AppConfig  # Importa la clase base AppConfig, que se usa para configurar una aplicación en Django


class AutoresConfig(AppConfig):  # Define una nueva clase llamada AutoresConfig, que hereda de AppConfig
    default_auto_field = 'django.db.models.BigAutoField'  
    # Establece el tipo de campo predeterminado para claves primarias automáticas en los modelos de esta aplicación.
    # 'BigAutoField' es un campo de enteros grandes que Django usará como ID para los modelos que no especifiquen uno.

    name = 'autores'  # Define el nombre de la aplicación. 
    # Este nombre debe coincidir con el nombre de la carpeta donde se encuentra la aplicación, 
    # y se utiliza para identificar esta aplicación en la configuración global de Django.
