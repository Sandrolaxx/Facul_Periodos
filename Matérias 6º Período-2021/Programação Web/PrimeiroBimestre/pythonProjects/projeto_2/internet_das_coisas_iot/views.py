from django.http.response import HttpResponse
from django.shortcuts import render

def method(request):
    return render(request, 'internet_das_coisas_iot/index.html')