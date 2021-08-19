# Python

## **Python - pip**

Gerenciador de pacotes
Utilizado por linha de comando

```
$ pip <argumentos>
```

---
<br>

## **Shell X Script**

No shell podemos testar comando curtos e realizar pequenos testes. Interação direta com o usuário.
<br> No Script podemos estruturar um programa com vários arqquivos. Interação através da compilação.

```
$ python <classe.py>
```

---
<br>

## **Estrutura**

Case sensitive
<br>Letras, números e underscore
<br>Palavras Reservadas:
and, as, assert, break, class, continue, def, del, elif, else, except, exec, finaly, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield, True, False, None.

--- 
<br>

## **Tipos Primitivos**

* Inteiro(int)
* Ponto flutuante(float)
* Lógico(bool)
* Caractere(str)

--- 
<br>

## **Funções de String**

* len -> tamanho do texto
* capitalize -> Primeira letra do texto para uppercase
* count -> conta determinado caratere no texto count('n')
* startswith -> retorno boolean se o texto começa com determinada letra
* endswith -> retorno boolean se o texto termina com determinada letra
* isalpha -> retorna boolean se o texto é uma string pura
* isalnum -> retorna boolean se o texto é alfanumerico
* islower -> retorna boolean se o texto é lowerCase
* isupper -> retorna boolean se o texto é upperCase
* lower -> retorna o texto em lowerCase
* upper -> retorna o texto em upperCase
* swapcase -> retorna o texto ao contrario Python -> pYTHON
* title -> upper na primeira letra de todas as palavras do texto
* split -> quebra as palavras em um array.
* replace(S1, S2) -> troca as palavras no texto
* find -> encontra a palavra informada no texto e retorna sua posição
* ljust -> justifica a esquerda com a quantidade de caracteres a ser adicionada
* rjust -> justifica a direita com a quantidade de caracteres a ser adicionada
* center -> centraliza o texto com a quantidade de caracteres em cada lado.

---
<br>

## **Controle de Fluxo**

Execução linha por linha
* Comando : para iniciar estrutura
* Identação é obrigatória
* Quebra da indentação indica fim da estrutura
* Não existe switch 

Ex condicional:

```python
x = int(input('digite um valor: '))

if x < 10:
    print('x<10')
else:
    print('x>=10')    
```

elif
```python
x = int(input('digite um valor: '))

if x < 10:
    print('x<10')
elif c<=10 and x>=5:
    print('x entre 10 e 5)    
else:
    print('x>=10')    
```

while
```python
x = 0

while i < 10:
    print(i)
    i += 1    
```

for
```python
for i in [0, 'a', 2, 4, 1]:
    print(i)    
```

for
```python
for i in renge(10):
    print(i)    
```

while import randint
```python
from random import randint

while True: 
    x = randint(0, 10)
    print(x)
    if x == 5:
        break
```