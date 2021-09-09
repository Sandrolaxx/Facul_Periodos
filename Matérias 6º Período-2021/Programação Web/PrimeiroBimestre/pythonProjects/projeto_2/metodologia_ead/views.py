from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19201 - Metodologia - EAD | Carga Horária:60h")