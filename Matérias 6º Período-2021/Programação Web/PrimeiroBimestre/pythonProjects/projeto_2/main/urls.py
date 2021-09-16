"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('desenvolvimento_para_dispositivos_moveis/', include('desenvolvimento_para_dispositivos_moveis.urls')),
    path('algoritimos_e_logica_de_programacao/', include('algoritimos_e_logica_de_programacao.urls')),
    path('banco_de_dados/', include('banco_de_dados.urls')),
    path('big_data/', include('big_data.urls')),
    path('calculo_diferencial_e_integral/', include('calculo_diferencial_e_integral.urls')),
    path('comunicacao_ead/', include('comunicacao_ead.urls')),
    path('desenvolvimento_para_jogos_digitais/', include('desenvolvimento_para_jogos_digitais.urls')),
    path('empreendedorismo_ead/', include('empreendedorismo_ead.urls')),
    path('engenharia_de_economica/', include('engenharia_de_economica.urls')),
    path('engenharia_de_software_analise_e_projeto_de_software/', include('engenharia_de_software_analise_e_projeto_de_software.urls')),
    path('engenharia_de_software_arquitetura_de_software/', include('engenharia_de_software_arquitetura_de_software.urls')),
    path('engenharia_de_software_metodos_de_desenvolvimento/', include('engenharia_de_software_metodos_de_desenvolvimento.urls')),
    path('engenharia_de_software_modelagem_de_software/', include('engenharia_de_software_modelagem_de_software.urls')),
    path('engenharia_de_software_processos_e_requisitos/', include('engenharia_de_software_processos_e_requisitos.urls')),
    path('engenharia_de_software_qualidade_de_software/', include('engenharia_de_software_qualidade_de_software.urls')),
    path('estagio_supervisionado_I/', include('estagio_supervisionado_I.urls')),
    path('estagio_supervisionado_II/', include('estagio_supervisionado_II.urls')),
    path('estrutura_de_dados/', include('estrutura_de_dados.urls')),
    path('filosofia_ead/', include('filosofia_ead.urls')),
    path('gestao_de_projetos/', include('gestao_de_projetos.urls')),
    path('inovacoes_tecnologicas/', include('inovacoes_tecnologicas.urls')),
    path('inteligencia_artificial/', include('inteligencia_artificial.urls')),
    path('interface_homem_computador/', include('interface_homem_computador.urls')),
    path('internet_das_coisas_iot/', include('internet_das_coisas_iot.urls')),
    path('introducao_a_engenharia_de_software/', include('introducao_a_engenharia_de_software.urls')),
    path('linguagem_de_programacao/', include('linguagem_de_programacao.urls')),
    path('logica_matematica/', include('logica_matematica.urls')),
    path('matematica_discreta/', include('matematica_discreta.urls')),
    path('metodologia_ead/', include('metodologia_ead.urls')),
    path('metodologias_ageis/', include('metodologias_ageis.urls')),
    path('organizacao_e_redes_de_computadores/', include('organizacao_e_redes_de_computadores.urls')),
    path('pesquisa_operacional/', include('pesquisa_operacional.urls')),
    path('probabilidade_estatistica/', include('probabilidade_estatistica.urls')),
    path('programaca_web/', include('programaca_web.urls')),
    path('projeto_de_designe_de_software/', include('projeto_de_designe_de_software.urls')),
    path('projeto_de_programacao_banco_de_dados/', include('projeto_de_programacao_banco_de_dados.urls')),
    path('projeto_desenvolvimento_professional_I/', include('projeto_desenvolvimento_professional_I.urls')),
    path('projeto_desenvolvimento_professional_II/', include('projeto_desenvolvimento_professional_II.urls')),
    path('projeto_integracao_software/', include('projeto_integracao_software.urls')),
    path('projeto_mineracao_dados/', include('projeto_mineracao_dados.urls')),
    path('projeto_orientado_a_objetos/', include('projeto_orientado_a_objetos.urls')),
    path('projeto_programacao_web/', include('projeto_programacao_web.urls')),
    path('sociologia_ead/', include('sociologia_ead.urls')),
    path('sustentabilidade_ead/', include('sustentabilidade_ead.urls'))
]
