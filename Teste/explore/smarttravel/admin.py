from django.contrib import admin
from .models import Categorias

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    # Personalize o comportamento do admin, se necessário
    list_display = ('id_categorias', 'categorias')
    search_fields = ['categorias']

