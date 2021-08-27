listaIdades = []
listaGeneros = []
listaSalarios = []
idade = 0

while idade >= 0:
    try:
        idade = int(input('Digite sua idade👉: '))

        if idade < 0:
            print('Valor negativo, encerrando o programa!')
            break
    except:
        print('🙅Valor inválido! Informe um número inteiro para idade!')
        break
    try:
        sexo = str(input('Digite seu Sexo(M/F)👉: '))
    except:
        print('🙅Valor inválido! Campo aceita somente (M/F)!')
        break
    try:
        salario = float(input('Digite seu salário👉: '))
    except:
        print('🙅Valor inválido! Informe um valor decimal!')
        break

    listaIdades.append(idade)
    listaGeneros.append(sexo)
    listaSalarios.append(salario)

indexMenorSalario = listaSalarios.index(min(listaSalarios))

print('\n💸Média Salarial do Grupo:', sum(listaSalarios) / len(listaSalarios))
print('Maior idade do grupo:', max(listaIdades), '| Menor Idade do Grupo:', min(listaIdades))
print('Quantidade de Homens:', listaGeneros.count('M'), ' | Quantidade de Mulheres:', listaGeneros.count('F'))
print('------------------------------------------------')
print('Dados da Pessoa Com Menor Salário')
print('Gênero:', listaGeneros[indexMenorSalario])
print('Idade:',  listaIdades[indexMenorSalario])