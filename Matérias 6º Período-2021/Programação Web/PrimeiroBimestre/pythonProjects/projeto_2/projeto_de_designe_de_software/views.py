from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'projeto_de_designe_de_software/index.html')