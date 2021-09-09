from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19303 - Engenharia de Software: Modelagem de Software | Carga Horária:80h")