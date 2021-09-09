from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19405 - Engenharia de Software: Métodos de Desenvolvimento | Carga Horária:80h")