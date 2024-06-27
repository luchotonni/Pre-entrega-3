from django.shortcuts import render, redirect

# Create your views here.
from .models import Cartera, Remera, Pulsera
from .forms import CarteraForm, RemeraForm, PulseraForm, BuscarForm


def lista_productos(request):
    carteras = Cartera.objects.all()
    remeras = Remera.objects.all()
    pulseras = Pulsera.objects.all()
    return render(request, 'catalogo/lista_productos.html', {'carteras': carteras, 'remeras': remeras, 'pulseras': pulseras})


def agregar_producto(request, tipo):
    if tipo == 'cartera':
        form = CarteraForm(request.POST or None)
    elif tipo == 'remera':
        form = RemeraForm(request.POST or None)
    elif tipo == 'pulsera':
        form = PulseraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_productos')

    return render(request, 'catalogo/agregar_producto.html', {'form': form, 'tipo': tipo})


def buscar_producto(request):
    form = BuscarForm(request.GET or None)
    resultados = None
    if form.is_valid():
        query = form.cleaned_data['query']
        resultados = {
            'carteras': Cartera.objects.filter(nombre__icontains=query),
            'remeras': Remera.objects.filter(nombre__icontains=query),
            'pulseras': Pulsera.objects.filter(nombre__icontains=query),
        }
    return render(request, 'catalogo/buscar_producto.html', {'form': form, 'resultados': resultados})
