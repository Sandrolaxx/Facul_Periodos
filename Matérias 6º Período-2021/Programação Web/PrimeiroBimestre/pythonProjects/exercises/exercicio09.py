print('🏦------SANDROLAX BANK------🏦')

saldoConta = 0.0
opcao = str

while opcao != 'd':

    print('a)Consulta Saldo')
    print('b)Saque')
    print('c)Depósito')
    print('d)Sair')

    print('---------------------------\n')

    opcao = str(input('Escolha uma Opção👉: '))

    if opcao == 'a':
        print('---------------------------')
        print('Saldo da Conta: R$', saldoConta)
        print('---------------------------')

    if opcao == 'b':
        print('---------------------------')
        print('Valor Disponível Para Saque: R$', saldoConta)
        print('---------------------------')
        saldoConta -= float(input('Valor do Saque👉: '))

    if opcao == 'c':
        print('---------------------------')
        saldoConta += float(input('Valor do Depósito👉: '))
        print('---------------------------')

    if opcao == 'd':
        break