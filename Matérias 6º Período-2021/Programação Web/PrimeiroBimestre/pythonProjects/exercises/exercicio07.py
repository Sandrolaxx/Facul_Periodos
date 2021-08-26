isNumeroInvalido = True

while isNumeroInvalido:
    try:
        valor = int(input('Digite um valor👉: '))
    except:
        print('🙅Valor inválido! Informe um número inteiro!')
        break

    if valor >= 12 and valor <= 20:
        print('⚡Número Válido:', valor)
        isNumeroInvalido = False
    else:
        print('❌Entrada inválida')