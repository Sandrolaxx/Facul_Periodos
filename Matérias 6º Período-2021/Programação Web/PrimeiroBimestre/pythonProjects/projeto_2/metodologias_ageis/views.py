from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19105 - Metodologias Ágeis | Carga Horária:80h")