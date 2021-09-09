from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19805 - Projeto de Desenvolvimento Profissional II | Carga Horária:40h")