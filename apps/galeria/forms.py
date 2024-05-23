from django import forms

from apps.galeria.models import Paciente

class PacienteForms(forms.ModelForm):
    class Meta:
        model = Paciente
        exclude = ['publicada',]
        labels = {
            'endereco':'Endereço',
            'numero': 'Número',
            'usuario': 'Entrevistador',
            'rg':'RG',
            'cpf':'CPF',
            'local_trabalho': 'Local de Trabalho',
            'grau_instrucao': 'Grau de Instrução',
            'renda_mensal': 'Renda Mensal',
            'estado_civil': 'Estado Civil',
            'auxilio_solicitado':'Auxílio Solicitado',
            'composicao_familiar': 'Composição familiar',
            'habitacao': 'Tipo de Habitação',
            'valor_habitacao': 'Caso alugada ou financianda, qual o valor pago mensalmente?',
            'saude': 'Possui algum tipo de previdência ou assistência?',
            'saude_familia': 'Problemas de saúde na família',
            'diagnostico': 'Diagnóstico',
            'providencia': 'Providência',
            'observacao': 'Observação',
        }
    
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'numero': forms.TextInput(attrs={'class':'form-control'}),
            'bairro': forms.TextInput(attrs={'class':'form-control'}),
            'idade': forms.TextInput(attrs={'class':'form-control'}),
            'data_nascimento': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
            'rg': forms.TextInput(attrs={'class':'form-control'}),
            'cpf': forms.TextInput(attrs={'class':'form-control'}),
            'local_trabalho': forms.TextInput(attrs={'class':'form-control'}),
            'grau_instrucao': forms.Select(attrs={'class':'form-control'}),
            'renda_mensal': forms.TextInput(attrs={'class':'form-control'}),
            'estado_civil': forms.Select(attrs={'class':'form-control'}),
            'auxilio_solicitado': forms.Select(attrs={'class':'form-control'}),
            'composicao_familiar': forms.Textarea(attrs={'class':'form-control'}),
            'habitacao': forms.Select(attrs={'class':'form-control'}),
            'valor_habitacao': forms.TextInput(attrs={'class':'form-control'}),
            'saude': forms.Select(attrs={'class':'form-control'}),
            'saude_familia': forms.TextInput(attrs={'class':'form-control'}),
            'diagnostico': forms.TextInput(attrs={'class':'form-control'}),
            'providencia': forms.TextInput(attrs={'class':'form-control'}),
            'data': forms.DateInput(
                format = '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'observacao': forms.Textarea(attrs={'class':'form-control'}),
        }
