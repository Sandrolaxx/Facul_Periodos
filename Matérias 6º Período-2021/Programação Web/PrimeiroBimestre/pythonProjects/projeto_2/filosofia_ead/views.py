from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19301 - Filosofia EAD | Carga Horária:60h")