print('🏦------SANDROLAX BANK------🏦')

qtdNotasDe2 = 0
qtdNotasDe5 = 0
qtdNotasDe10 = 0
qtdNotasDe20 = 0
qtdNotasDe50 = 0
qtdNotasDe100 = 0

valorSaque = float(input('Valor do Saque👉: '))

while valorSaque > 0:

    if valorSaque % 100 == 0:
        qtdNotasDe100 += 1
        valorSaque -= 100

    elif valorSaque % 50 == 0:
        qtdNotasDe50 += 1
        valorSaque -= 50

    elif valorSaque % 20 == 0:
        valorSaque -= 20
        qtdNotasDe20 += 1

    elif valorSaque % 10 == 0:
        qtdNotasDe10 += 1
        valorSaque -= 10

    elif valorSaque % 5 == 0:
        qtdNotasDe5 += 1
        valorSaque -= 5

    elif valorSaque % 2 == 0:
        qtdNotasDe2 += 1
        valorSaque -= 2

    else:
        print('🙅Valor Inválido!')
        break    


if qtdNotasDe2 > 0:
    print('--------------------💸---------------------')
    print('Quantidade de notas de R$ 2,00:', qtdNotasDe2)
if qtdNotasDe5 > 0:
    print('--------------------💸---------------------')
    print('Quantidade de notas de R$ 5,00:', qtdNotasDe5)
if qtdNotasDe10 > 0:
    print('--------------------💸---------------------')
    print('Quantidade de notas de R$ 10,00', qtdNotasDe10)
if qtdNotasDe20 > 0:
    print('--------------------💸---------------------')
    print('Quantidade de notas de R$ 20,00', qtdNotasDe20)
if qtdNotasDe50 > 0:
    print('--------------------💸---------------------')
    print('Quantidade de notas de R$ 50,00', qtdNotasDe50)
if qtdNotasDe100 > 0:
    print('--------------------💸---------------------')
    print('Quantidade de notas de R$ 100,00', qtdNotasDe100)
              
