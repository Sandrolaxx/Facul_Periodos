from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'projeto_desenvolvimento_professional_I/index.html')