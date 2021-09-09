from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19305 - Projeto Orientado a Objetos | Carga Horária:100h")