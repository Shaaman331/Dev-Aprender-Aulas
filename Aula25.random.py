'''
* Python tem um módulo embutido que você pode usar para fazer números aleatórios.

* Para utilizarmos as funções disponíveis no módulo random, devemos adicionar no início do código 
a importação do recurso por meio do comando “import random” e utilizamos a classe random, que 
contém um conjunto de métodos para gerar ou manipular dados aleatoriamente.
O randommódulo tem um conjunto de métodos: 

* A função random.random() para exibirmos um número aleatório com base no valor inicial.
* A função random.randint() retorna um número inteiro aleatório entre um determinado intervalo.
* A função random.choice() retorna um elemento aleatório que pertença a uma sequência, que pode 
ser uma variável do tipo string, uma lista, uma tupla ou uma sequência numérica. 
* A função random.uniform() retorna um número decimal aleatório de acordo com os valores iniciais 
e finais definidos na função. 
* A função random.shuffle() é utilizada para exibir o resultado de uma lista ou de uma tupla de forma embaralhada.


1 - Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
2 - Vcoê quer fazer um sorteio entre 300 nomes em uma lista de nomes
3 - Você quer escolher aleatóriamente um número de 10-100
4 - Você quer escolher uma carta aleatóriamente dentro de um baralho 
5 - Você qier gerar nomes de um usuário aleatóriamente 
6 - Você quer gerar senhas seguras 



'''

import random

print(random.random()) # Valor 0.0 até 1.0
print(random.uniform(4,10)) # Valor decimal do mínimo ao máximo.
print(random.randint(12,55)) # Valor inteiro do mínimo ao máximo.
print()

print('Sorteio de cores com random choice')
cores = ['verde','vermelho','azul']
print(random.choice(cores)) # Retorna um elemento aleatório que pertença a uma sequência.
print()

print('Sorteio de cartas de um baralho com random shurfle')
cartas_de_baralho = ['carta1', 'carta2', 'carta3','carta4']
random.shuffle(cartas_de_baralho) # Exibi o resultado de uma lista ou de uma tupla de forma embaralhada.
print(cartas_de_baralho)
print()

print('Sortear moeda')
moeda = ['cara', 'coroa']
print(random.choice(moeda)) # Retorna um elemento aleatório que pertença a uma sequência
print()

print('Random Choice')
lista_nomes=['Maria', 'João', 'Pedro', 'Cláudia']
print(random.choice(lista_nomes)) # Retorna um elemento aleatório que pertença a uma sequência
print()

print('Retorna elemento aleatório com Random Choice')
nome = 'Ivani'
print(random.choice(nome)) # Retorna um elemento aleatório que pertença a uma sequência
print()

print('Tuplas com Random Choice')
tupla_nomes=('Maria', 'João', 'Pedro', 'Cláudia')
print(random.choice(tupla_nomes)) # Retorna um elemento aleatório que pertença a uma sequência

print('Dicionário com Rando Choice')
lista_dicionario_nomes= [{"nome": "Maria", "idade": 20}, {"nome": "Cláudia", "idade": 20}]
print(random.choice(lista_dicionario_nomes))
print()

print('Range com Random Choite')
print(random.choice(range(2,20)))
