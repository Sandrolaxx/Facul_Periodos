from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19606 - Estágio Supervisionado II | Carga Horária:40h")