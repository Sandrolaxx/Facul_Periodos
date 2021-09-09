from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19205 - Estrutura de Dados | Carga Horária:80h")