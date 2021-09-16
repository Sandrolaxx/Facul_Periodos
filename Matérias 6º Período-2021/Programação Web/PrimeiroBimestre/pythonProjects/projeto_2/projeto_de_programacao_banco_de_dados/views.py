from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'projeto_de_programacao_banco_de_dados/index.html')