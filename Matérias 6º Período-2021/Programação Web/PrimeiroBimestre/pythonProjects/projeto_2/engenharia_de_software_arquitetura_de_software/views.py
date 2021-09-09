from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19604 - Engenharia de Software: Arquitetura de Software | Carga Horária:40h")