from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19102 - Introdução a Engenharia de Software | Carga Horária:80h")