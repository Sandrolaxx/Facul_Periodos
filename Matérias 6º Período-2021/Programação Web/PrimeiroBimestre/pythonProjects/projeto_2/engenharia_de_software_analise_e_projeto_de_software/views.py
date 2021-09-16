from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'engenharia_de_software_analise_e_projeto_de_software/index.html')