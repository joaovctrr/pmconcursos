from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cpf', 'telefone')
    search_fields = ('usuario__username', 'cpf')
    list_filter = ('data_nascimento',)