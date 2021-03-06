from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administracao/', views.administracao, name='administracao'),
    path('agronomia/', views.agronomia, name='agronomia'),
    path('arquitetura/', views.arquitetura, name='arquitetura'),
    path('ciencias-biologicas/', views.cienciasBiologicas, name='ciencias-biologicas'),
    path('ciencias-contabeis/', views.cienciasContabeis, name='ciencias-contabeis'),
    path('design-grafico/', views.designGrafico, name='design-grafico'),
    path('direito/', views.direito, name='direito'),
    path('educacao-fisica/', views.educacaoFisica, name='educacao-fisica'),
    path('enfermagem/', views.enfermagem, name='enfermagem'),
    path('engenharia-civil/', views.engenhariaCivil, name='engenharia-civil'),
    path('engenharia-de-controle-e-automacao/', views.engenhariaDeControleAutomacao, name='engenharia-de-controle-e-automacao'),
    path('engenharia-software/', views.engenhariaSoftware, name='engenharia-software'),
    path('engenharia-eletrica/', views.engenhariaEletrica, name='engenharia-eletrica'),
    path('engenharia-mecanica/', views.engenhariaMecanica, name='engenharia-mecanica'),
    path('mecatronica/', views.mecatronica, name='mecatronica'),
    path('farmacia/', views.farmacia, name='farmacia'),
    path('fisioterapia/', views.fisioterapia, name='fisioterapia'),
    path('fonoaudiologia/', views.fonoaudiologia, name='fonoaudiologia'),
    path('fotografia/', views.fotografia, name='fotografia'),
    path('historia/', views.historia, name='historia'),
    path('jornalismo/', views.jornalismo, name='jornalismo'),
    path('letras-espanhol/', views.letrasEspanhol, name='letras-espanhol'),
    path('letras/', views.letras, name='letras'),
    path('medicina/', views.medicina, name='medicina'),
    path('medicina-veterinaria/', views.medicinaVeterinaria, name='medicina-veterinaria'),
    path('nutricao/', views.nutricao, name='nutricao'),
    path('pedagogia/', views.pedagogia, name='pedagogia'),
    path('producao-audiovisual/', views.producaoAudiovisual, name='producao-audiovisual'),
    path('producao-multimidia/', views.producaoMultimidia, name='producao-multimidia'),
    path('psicologia/', views.psicologia, name='psicologia'),
    path('publicidade-e-propaganda/', views.publicidadePropaganda, name='publicidade-e-propaganda'),
    path('sistemas-de-informacao/', views.sistemasInformacao, name='sistemas-de-informacao')
]