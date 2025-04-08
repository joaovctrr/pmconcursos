# cursos/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome

class Matricula(models.Model):
    aluno = models.ForeignKey(User, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=1,
        choices=[('A', 'Ativa'), ('C', 'Concluída')],
        default='A'
    )
    
    def __str__(self):
        return f"{self.aluno.username} - {self.curso.nome}"