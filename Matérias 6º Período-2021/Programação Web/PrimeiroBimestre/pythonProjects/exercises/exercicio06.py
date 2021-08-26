listaNoIntervalo = []
listaForaIntervalo = []
numerosNoIntervalo = int(0)
numerosForaDoIntervalo = int(0)

for i in range(10):
    try:
        valor = int(input('Digite um valor👉: '))
    except:
        print('🙅Valor inválido! Informe um número inteiro!')
        break

    if valor >= 10 and valor <= 20:
        listaNoIntervalo.append(valor)
        numerosNoIntervalo += 1
    else:
        listaForaIntervalo.append(valor)
        numerosForaDoIntervalo += 1
        
print('\nQuantidade de Números Dentro do Intervalo(10 até 20): ', numerosNoIntervalo)
print('💣Lista dos Números Dentro do Intervalo(10 até 20):')
print(listaNoIntervalo)
print('\nQuantidade de Números Fora do Intervalo(10 até 20): ', numerosForaDoIntervalo)
print('💥Lista dos Números Fora do Intervalo(10 até 20):')
print(listaForaIntervalo)