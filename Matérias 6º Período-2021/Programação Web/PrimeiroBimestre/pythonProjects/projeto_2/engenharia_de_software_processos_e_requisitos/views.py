from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19204 - Engenharia de Software: Processos e Requisitos | Carga Horária:80h")