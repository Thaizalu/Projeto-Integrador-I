from django.urls import path
from apps.galeria.views import \
     index, paciente, buscar, novo_paciente, editar_ficha, deletar_paciente, filtro

urlpatterns = [
    path('', index, name='index'),
    path('paciente/<int:foto_id>', paciente, name='paciente'),
    path('buscar', buscar, name='buscar'),
    path('novo-paciente', novo_paciente, name='novo_paciente'),
    path('editar_ficha/<int:foto_id>/', editar_ficha, name='editar_ficha'),
    path('deletar-paciente/<int:foto_id>', deletar_paciente, name='deletar_paciente')
]