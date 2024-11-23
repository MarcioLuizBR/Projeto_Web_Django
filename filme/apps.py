from django.apps import AppConfig


class FilmeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filme'
    
    
    # # para criação do super usuario no deploy do site
    # def ready(self):
    #     from .models import Usuario
    #     import os
        
    #     # criar no servidor estas variaveis - EMAIL_ADMIN / SENHA_ADMIN
    #     email = os.getenv("EMAIL_ADMIN")
    #     senha = os.getenv("SENHA_ADMIN")
        
    #     usuarios = Usuario.objects.filter(email=email)
    #     if not usuarios:
    #         Usuario.objects.create_superuser(username="admin", email=email, password=senha, is_active=True, is_staff=True)