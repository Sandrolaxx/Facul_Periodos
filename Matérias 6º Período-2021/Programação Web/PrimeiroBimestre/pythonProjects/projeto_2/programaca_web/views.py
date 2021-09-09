from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19602 - Programação Web | Carga Horária:80h")