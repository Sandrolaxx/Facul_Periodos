from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19206 - Linguagem de Programação | Carga Horária:80h")