from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19505 - Projeto de Banco de Dados | Carga Horária:100h")