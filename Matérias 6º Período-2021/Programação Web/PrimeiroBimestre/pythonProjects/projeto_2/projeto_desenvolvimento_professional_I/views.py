from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19704 - Projeto de Desenvolvimento Profissional I | Carga Horária:40h")