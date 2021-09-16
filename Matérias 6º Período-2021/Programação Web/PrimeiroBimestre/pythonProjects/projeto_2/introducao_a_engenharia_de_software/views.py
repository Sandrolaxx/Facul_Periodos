from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'introducao_a_engenharia_de_software/index.html')