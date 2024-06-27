from django import forms
from .models import Cartera, Remera, Pulsera


class CarteraForm(forms.ModelForm):
    class Meta:
        model = Cartera
        fields = ['nombre', 'precio', 'descripcion']


class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remera
        fields = ['nombre', 'precio', 'descripcion']


class PulseraForm(forms.ModelForm):
    class Meta:
        model = Pulsera
        fields = ['nombre', 'precio', 'descripcion']


class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)
