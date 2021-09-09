from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19804 - Internet das Coisas IoT | Carga Horária:80h")