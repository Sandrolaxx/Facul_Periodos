from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19701 - Desenvolvimento para Jogos Digitais | Carga Horária:80h")