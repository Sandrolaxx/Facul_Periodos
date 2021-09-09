from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19104 - Lógica Matemática | Carga Horária:80h")