from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19803 - Inovações Tecnológicas | Carga Horária:40h")