from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'calculo_diferencial_e_integral/index.html')