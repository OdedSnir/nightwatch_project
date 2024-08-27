from django.apps import AppConfig

#configuration class for my application
class MyappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "myapp"
