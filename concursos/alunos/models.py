from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username