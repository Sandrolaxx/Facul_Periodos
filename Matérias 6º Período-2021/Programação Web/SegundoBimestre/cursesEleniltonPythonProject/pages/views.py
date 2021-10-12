from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def administracao(request):
    return render(request, 'pages/administracao.html')