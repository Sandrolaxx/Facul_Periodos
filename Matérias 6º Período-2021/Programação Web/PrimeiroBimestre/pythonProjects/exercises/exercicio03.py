try:
    x = int(input('Digite um valor👉: '))
except:
    print('🙅Valor inválido! Informe um número inteiro!')

if x >= 1 and x <= 10:
    for i in range(10):
        print((i + 1) * x) 
else:
    print('Valor informado inválido!😕👎')