from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: Algoritmos e Lógica de Programação | Carga Horária:80h")