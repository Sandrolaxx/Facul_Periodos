from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'organizacao_e_redes_de_computadores/index.html')