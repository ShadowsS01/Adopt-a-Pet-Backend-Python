from django.contrib import admin
from .models import Adocao


@admin.register(Adocao)
class AdocaoAdmin(admin.ModelAdmin):
    list_display = ("pet", "email", "valor")
    list_filter = ("pet", "email", "valor")
