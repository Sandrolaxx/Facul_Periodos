from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19302 - Matemática Discreta | Carga Horária:40h")