from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19506 - Estágio Supervisionado I | Carga Horária:40h")