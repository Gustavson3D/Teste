from django.contrib import admin
from .models import Categorias, Cidade, Local

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    # Personalize o comportamento do admin, se necessário
    list_display = ('id_categorias', 'categorias')
    search_fields = ['categorias']


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_cidade', 'descricao')  # Exibir esses campos na lista de cidades no admin

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome_local', 'descricao', 'cidade', 'bairro', 'rua', 'telefone', 'tipo')  # Exibir esses campos na lista de locais no admin
    list_filter = ('cidade', 'tipo')  # Adicionar filtros por cidade e tipo
    search_fields = ('nome_local', 'descricao', 'bairro', 'rua')  # Adicionar campo de pesquisa

admin.site.register(Cidade, CidadeAdmin)


