from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('nuevo/', nuevo),
    path('usado/', usado),
    path('busca/', busca),
    path('buscar/', buscar),
    path('lista-nuevos/', lista_nuevos),
    path('lista-usados/', lista_usados),
]