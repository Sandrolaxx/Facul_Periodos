from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'inovacoes_tecnologicas/index.html')