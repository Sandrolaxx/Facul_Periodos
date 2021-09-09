from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19406 - Projeto de Design de Software | Carga Horária:100h")