mediaIdade = int
listaIdades = []

for i in range(10):
    try:
        idade = int(input('Digite sua idade👉: '))
    except:
        print('🙅Idade inválida! Informe um número inteiro!')
        break
    listaIdades.append(idade)
    
print('\n🏁Média:')
print(sum(listaIdades) / len(listaIdades))