from django.http.response import HttpResponse

def index(request):
    return HttpResponse("Matéria: EGS19703 - Engenharia de Software: Qualidade de Software (Gestão de Configuração e Mudanças) | Carga Horária:80h")