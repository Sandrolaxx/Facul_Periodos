listaImpares = []
listaPares = []

for i in range(10):
    try:
        valor = int(input('Digite um valor👉: '))
    except:
        print('🙅Valor inválido! Informe um número inteiro!')
        break

    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)
        
print('\n💣Lista dos Números Impares:')
print(listaImpares)
print('\n💥Lista dos Números Pares:')
print(listaPares)