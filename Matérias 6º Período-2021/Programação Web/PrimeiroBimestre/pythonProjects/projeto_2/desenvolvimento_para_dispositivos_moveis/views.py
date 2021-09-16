from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'desenvolvimento_para_dispositivos_moveis/index.html')