from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19203 - Organização e Redes de Computadores | Carga Horária:40h")