from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19202 - Cálculo Diferencial e Integral | Carga Horária:40h")