from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19801 - Inteligência Artificial | Carga Horária:80h")