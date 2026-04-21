from django.shortcuts import render, redirect
from .forms import *
from .models import *

def inicio(request):
    return render(request, "app/inicio.html")

def nuevo(request):
    form = NuevoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "app/form.html", {"form": form, "titulo": "PERIFERICOS NUEVOS"})

def usado(request):
    form = UsadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "app/form.html", {"form": form, "titulo": "PERIFERICOS USADOS"})

def busca(request):
    form = BuscaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "app/form.html", {"form": form, "titulo": "SE BUSCA"})

def buscar(request):
    query = request.GET.get("modelo", "")

    resultados_nuevos = PerifericosNuevos.objects.filter(modelo__icontains=query)
    resultados_usados = PerifericosUsados.objects.filter(modelo__icontains=query)
    resultados_busca = SeBusca.objects.filter(modelo__icontains=query)

    return render(request, "app/buscar.html", {
        "query": query,
        "nuevos": resultados_nuevos,
        "usados": resultados_usados,
        "busca": resultados_busca
    })

def lista_nuevos(request):
    datos = PerifericosNuevos.objects.all()
    return render(request, "app/lista.html", {"datos": datos, "titulo": "NUEVOS"})

def lista_usados(request):
    datos = PerifericosUsados.objects.all()
    return render(request, "app/lista.html", {"datos": datos, "titulo": "USADOS"})