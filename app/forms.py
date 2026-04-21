from django import forms
from .models import *

class NuevoForm(forms.ModelForm):
    class Meta:
        model = PerifericosNuevos
        fields = '__all__'

class UsadoForm(forms.ModelForm):
    class Meta:
        model = PerifericosUsados
        fields = '__all__'

class BuscaForm(forms.ModelForm):
    class Meta:
        model = SeBusca
        fields = '__all__'

class BuscarForm(forms.Form):
    modelo = forms.CharField(max_length=100)