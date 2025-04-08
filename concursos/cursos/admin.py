from django.contrib import admin
from .models import Curso, Matricula

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'ativo')
    search_fields = ('nome',)

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'status')
    list_filter = ('status',)