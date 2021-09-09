from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19502 - Engenharia de Software: Análise e Projeto de Software | Carga Horária:80h")