from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19503 - Banco de Dados | Carga Horária:80h")