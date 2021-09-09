from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19802 - Big Data | Carga Horária:40h")