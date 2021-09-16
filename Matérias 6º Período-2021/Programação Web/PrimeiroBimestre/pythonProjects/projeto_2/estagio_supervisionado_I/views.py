from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'estagio_supervisionado_I/index.html')