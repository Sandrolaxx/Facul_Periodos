from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19101 - Comunicação - EAD | Carga Horária:60h")