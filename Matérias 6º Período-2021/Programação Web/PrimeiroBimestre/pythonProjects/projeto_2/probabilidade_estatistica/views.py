from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19504 - Probabilidade e Estatística | Carga Horária:40h")