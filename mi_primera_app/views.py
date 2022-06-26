from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    fecha_hora_ahora = datetime.now()
    return HttpResponse(f'hola mundo {fecha_hora_ahora}')


def otro_saludo(request, nombre):
    return HttpResponse(f'hola {nombre.capitalize()}! como estas?')
