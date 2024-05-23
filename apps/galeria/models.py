from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Paciente(models.Model):

    OPCOES_AUXILIO_SOLICITADO = [
        ("CESTA BÁSICA","Cesta Básica"),
        ("LEITE","Leite"),
        ("SUPLEMENTO","Suplemento"),
        ("MEDICAMENTOS","Medicamentos"),
        ("OUTROS","Outros"),
    ]

    OPCOES_ESTADO_CIVIL = [
        ("SOLTEIRO","Solteiro"),
        ("CASADO","Casado"),
        ("UNIÃO ESTÁVEL","União Estável"),
        ("SEPARADO","Separado"),
        ("DIVORCIADO","Divorciado"),
        ("VIÚVO","Viúvo"),
    ]

    OPCOES_GRAU_INSTRUCAO = [
        ("SEM INSTRUÇÃO","Sem Instrução"),
        ("FUNDAMENTAL INCOMPLETO","Fundamental Incompleto"),
        ("FUNDAMENTAL COMPLETO","Fundamental Completo"),
        ("MÉDIO INCOMPLETO","Médio Incompleto"),
        ("MÉDIO COMPLETO","Médio Completo"),
        ("SUPERIOR INCOMPLETO","Superior Incompleto"),
        ("SUPERIOR COMPLETO","Superior Completo"),
    ]

    OPCOES_HABITACAO = [
        ("PRÓPRIA","Própria"),
        ("ALUGADA","Alugada"),
        ("FINANCIADA","Financiada"),
        ("CEDIDA","Cedida"),
    ]

    OPCOES_PREVIDENCIA = [
        ("INSS","INSS"),
        ("FUNERAL","Funeral"),
        ("OUTRA","Outra"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.CharField(max_length=150, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False, default='')
    bairro = models.CharField(max_length=100, null=True, blank=False)
    idade = models.CharField(max_length=50, null=False, blank=False, default='')
    data_nascimento = models.DateTimeField(default=datetime.now, blank=False)
    telefone = models.CharField(max_length=50, null=True, blank=False)
    rg = models.CharField(max_length=50, null=False, blank=False, default='')
    cpf = models.CharField(max_length=50, null=False, blank=False, default='')
    local_trabalho = models.CharField(max_length=50, null=True, blank=False)
    grau_instrucao = models.CharField(max_length=100, choices=OPCOES_GRAU_INSTRUCAO, default='')
    renda_mensal = models.CharField(max_length=50, null=False, blank=False, default='')
    estado_civil = models.CharField(max_length=100, choices=OPCOES_ESTADO_CIVIL, default='')
    auxilio_solicitado = models.CharField(max_length=100, choices=OPCOES_AUXILIO_SOLICITADO, default='')
    composicao_familiar = models.TextField(null=False, blank=False, default='')
    habitacao = models.CharField(max_length=100, choices=OPCOES_HABITACAO, default='')
    valor_habitacao = models.CharField(max_length=50, null=False, blank=False, default='')
    saude = models.CharField(max_length=100, choices=OPCOES_PREVIDENCIA, default='')
    saude_familia = models.CharField(max_length=255, null=False, blank=False, default='')
    diagnostico = models.CharField(max_length=255, null=False, blank=False, default='')
    providencia = models.CharField(max_length=255, null=False, blank=False, default='')
    publicada = models.BooleanField(default=True)
    data = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='user'
    )
    observacao = models.TextField(null=False, blank=False, default='')
 