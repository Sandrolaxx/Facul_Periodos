from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19404 - Engenharia Econômica | Carga Horária:40h")