from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19402 - Pesquisa Operacional | Carga Horária:40h")