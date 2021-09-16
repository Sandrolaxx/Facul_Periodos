from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'projeto_programacao_web/index.html')