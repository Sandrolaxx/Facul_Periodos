from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19603 - Gestão de Projetos | Carga Horária:80h")