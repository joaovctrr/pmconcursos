# questoes/admin.py
from django.contrib import admin
from .models import Subject, Question, Alternative  # Nomes em inglês

class AlternativeInline(admin.TabularInline):
    model = Alternative
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AlternativeInline]
    list_display = ('statement', 'subject', 'level', 'created_at')
    list_filter = ('subject', 'level')

admin.site.register(Subject)
admin.site.register(Alternative)