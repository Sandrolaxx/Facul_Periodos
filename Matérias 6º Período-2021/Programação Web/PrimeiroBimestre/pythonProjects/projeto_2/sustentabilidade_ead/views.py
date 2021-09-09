from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19501 - Sustentabilidade - EAD | Carga Horária:60h")