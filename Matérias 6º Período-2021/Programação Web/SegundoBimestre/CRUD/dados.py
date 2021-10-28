from contextlib import contextmanager

import pymysql.cursors

# CRUD - CREATE, READ, UPDATE, DELETE

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='localhost',
        user='sandrolax',
        password='1329',
        db='sandrolax_db'
    )

    try:
        yield conexao
    finally:
        conexao.close()

opcao = str

while opcao != 'e':   

    print('\n---------------------------')
    print('a)Inserir Nova Pessoa')
    print('b)Listar Dados da Agenda')
    print('c)Atualizar Dados Pessoa')
    print('d)Remover Pessoa Por Id')
    print('e)Sair')
    print('---------------------------\n')

    opcao = str(input('Escolha uma Opção👉: '))

    if opcao == 'a':
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                nome = input('Informe seu nome: ')
                telefone = input('Informe seu telefone: ')
                email = input('Informe seu e-mail: ')
                idade = int(input('Informe sua idade: '))
                sql = 'INSERT INTO agenda (nome, telefone, email, idade) VALUES ' \
                    '(%s, %s, %s, %s)'
                cursor.execute(sql, (nome, telefone, email, idade))
                conexao.commit()
    if opcao == 'b':
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM agenda')
                resultado = cursor.fetchall()

                print('Lista da galera:')
                for linha in resultado:
                    print(linha)
    if opcao == 'c':
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                id = int(input('Informe o id do usuário a ser atualizado: '))
                nome = input('Informe o novo nome: ')
                telefone = input('Informe o novo telefone: ')
                email = input('Informe o novo e-mail: ')
                idade = int(input('Informe a o nova idade: '))
                sql = 'UPDATE agenda SET nome=%s, telefone=%s, email=%s, idade=%s WHERE id=%s'
                cursor.execute(sql, (nome, telefone, email, idade, id))
                conexao.commit()
    if opcao == 'd':
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                id = int(input('Informe o id do usuário a ser deletado: '))
                sql = 'DELETE FROM agenda WHERE id = %s'
                cursor.execute(sql, (id))
                conexao.commit()
    if opcao == 'e':
        break

