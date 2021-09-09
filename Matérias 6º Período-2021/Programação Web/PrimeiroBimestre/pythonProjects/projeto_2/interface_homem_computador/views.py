from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19403 - Interface Homem Computador | Carga Horária:40h")