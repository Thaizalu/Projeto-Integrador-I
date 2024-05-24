from django.shortcuts import render, get_object_or_404, redirect
from apps.gacci.models import Paciente
from apps.gacci.forms import PacienteForms

from django.contrib import messages


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    pacientes = Paciente.objects.order_by("data").filter(publicada=True)
    return render(request, 'gacci/index.html', {"cards": pacientes})


def paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    return render(request, 'gacci/paciente.html', {"Paciente": paciente})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    pacientes = Paciente.objects.order_by("data").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            pacientes = pacientes.filter(nome__icontains=nome_a_buscar)

    return render(request, "gacci/index.html", {"cards": pacientes})


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

    return render(request, 'gacci/novo_paciente.html', {'form': form})


def editar_ficha(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    if request.method == 'POST':
        form = PacienteForms(request.POST, request.FILES, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Página atualizada com sucesso!')
            return redirect('index')
    else:
        form = PacienteForms(instance=paciente)

    return render(request, 'gacci/editar_ficha.html', {'form': form, 'paciente_id': paciente_id})


def deletar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    paciente.delete()
    messages.success(request, 'Página apagada com sucesso!')
    return redirect('index')


def filtro(request, categoria):
    pacientes = Paciente.objects.order_by("data").filter(publicada=True, categoria=categoria)
    return render(request, 'gacci/index.html', {"cards": pacientes})
