from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19806 - Projeto de Mineração de Dados | Carga Horária:120h")