from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Paciente
from apps.galeria.forms import PacienteForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    pacientes = Paciente.objects.order_by("data").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": pacientes})

def paciente(request, foto_id):
    paciente = get_object_or_404(Paciente, pk=foto_id)
    return render(request, 'galeria/paciente.html', {"Paciente": paciente})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    pacientes = Paciente.objects.order_by("data").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            pacientes = pacientes.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": pacientes})

def novo_paciente(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    if request.method == 'POST':
        form = PacienteForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente cadastrado com sucesso!')
            return redirect('index')       
    else:
        form = PacienteForms()

    return render(request, 'galeria/novo_paciente.html', {'form': form})

def editar_ficha(request, foto_id):
    paciente = get_object_or_404(Paciente, pk=foto_id)
    if request.method == 'POST':
        form = PacienteForms(request.POST, request.FILES, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Página atualizada com sucesso!')
            return redirect('index')
    else:
        form = PacienteForms(instance=paciente)

    return render(request, 'galeria/editar_ficha.html', {'form': form, 'foto_id': foto_id})

def deletar_paciente(request, foto_id):
    paciente = get_object_or_404(Paciente, pk=foto_id)
    paciente.delete()
    messages.success(request, 'Página apagada com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    pacientes = Paciente.objects.order_by("data").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": pacientes})