from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'engenharia_de_software_modelagem_de_software/index.html')