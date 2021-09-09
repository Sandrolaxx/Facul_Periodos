from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19401 - Sociologia - EAD | Carga Horária:60h")