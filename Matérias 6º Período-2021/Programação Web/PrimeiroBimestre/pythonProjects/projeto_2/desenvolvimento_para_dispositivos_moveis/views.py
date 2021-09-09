from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: Desenvolvimento Para Dispositivos Moveis | Carga Horária:80h")