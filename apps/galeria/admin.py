from django.contrib import admin

from apps.galeria.models import Paciente

class ListandoPacientes(admin.ModelAdmin):
    list_display = ("id", "nome", "endereco", "publicada")
    list_display_links = ("id","nome")
    search_fields = ("nome",)
    list_filter = ("auxilio_solicitado", 'usuario')
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Paciente, ListandoPacientes)
