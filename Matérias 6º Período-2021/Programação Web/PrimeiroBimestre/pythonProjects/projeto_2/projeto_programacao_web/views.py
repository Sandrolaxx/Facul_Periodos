from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19605 - Projeto de Programação Web | Carga Horária:120h")