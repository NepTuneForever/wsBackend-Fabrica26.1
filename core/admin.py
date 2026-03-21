from django.contrib import admin
from .models import Cripto, Favorito

@admin.register(Cripto)
class CriptoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'simbolo', 'preco')
    search_fields = ('nome', 'simbolo')

@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'simbolo', 'preco')
    search_fields = ('nome', 'simbolo')