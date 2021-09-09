from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19601 - Empreendedorismos - EAD | Carga Horária:60h")