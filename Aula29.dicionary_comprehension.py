'''
Dicionary Comprehension
* Dict Comprehensions foram introduzidas na linguagem através da especificação PEP 274.

Sua sintaxe básica é:
{chave: valor for elemento in iteravel}

Conceitos
* Chave: será a chave de cada elemento do dicionário resultante.
* Valor: valor daquela chave.
* Elemento: é a unidade de iteração do iterável iterável (se for uma lista, por exemplo, elemento irá receber o valor iteração à iteração)
* Iteravel: conjunto de dados que estão sendo iterados (pode ser uma lista ou um set, por exemplo)

Pra esclarecer, vamos à um exemplo:
dicionario = {elemento: elemento*2 for elemento in range(6)}

cada elemento da lista resultante de range(6) (0, 1, 2, 3, 4, 5) será convertido em:

Uma chave com o mesmo valor do elemento da lista.
elemento*2 é o valor de cada chave (multiplicar por 2 cada elemento).

Dict Comprehensions com if
* Podemos adicionar lógica condicional à construção do dicionário resultante do nosso Dict Comprehension.
* Podemos adicionar uma expressão condicional em três posições distintas:

Na construção da chave. Sintaxe:
{chave if condicao: valor for elemento in iteravel}

Na expressão que definirá o valor da chave:
{chave: valor if condicao for elemento in iteravel}

Ao final da expressão, filtrando os dados do iterável:
{chave: expressao for elemento in iteravel if condicao}

Dict Comprehensions com vários if


'''

#[expressão for membro in iterável]
#{chave:expressão for membro in iterável}

from pprint import pprint
import random
print('Dicionary Comprehension')
#{chave:expressão for membro in interavel}
pprint({i : i for i in range(20)})
print()

print('Populando um Dicionario com valores')
produtos = ['arroz','feijão','leite','macarrão','açucar']
#{chave:expressão for membro in interável}
pprint({produtos: 1 for produtos in produtos})
print()

print('Gerando uma matriz de valores de test')
#{chave:expressão for membro in interável}
pprint({produto: [0 for i in range(5)]for produto in produtos})
print()

print('Gerando multiplos de valores de test')

#{chave:expressão for membro in interável}
print({produto: [i * 2 for i in range(5)]for produto in produtos})
print()

print('Gerando valores aleatórios com range')

#{chave:expressão for membro in interável}
pprint({produto: [random.randint(1000, 1500) for i in range(5)]for produto in produtos})
print()

print('Desafio 1')
sorteios =['sorteio1', 'sorteio2', 'sorteio3']
participantes = ['Joel','Jessica','Lucca','Raquel','Marcos','John','Cris','Daneil']

# Declamos uma 2 listas sorteiso e participantes
# Passamos a chave {sorteio: random.choice(participantes)} para gerar ganhador aleatorio dentro de uma lista de possibilidades
# A expressão está acontecendo dentro da lista sorteio para todas as listas de sorteios "for in sorteio in sorteios"  
pprint({sorteio: random.choice(participantes)for sorteio in sorteios})
print()

print('Desafio 2')
grupos = ['grupo1','grupo2','grupo3']
# Definimos quais grupos participantes gerando um dicionário
# Passsamos a chave "{grupo: [random.randint(1 , 101)]}"  para gerar valores até 100
# Farems isso 5x usando "for i in range(5)" passando o interável pelo range
# A expressão está acontecendo dentro da lista grupo para todas as listas de grupos "for grupo in grupos"
pprint({grupo:[random.randint(1 , 101) for i in range(5)] for grupo in grupos})
print()

print('Manipulação com f strings')
lista = ['Ferrari', 'Lamborghini', 'Porsche']
dicionario = {
  f'{elemento.lower()}': f'Montadora: {elemento.upper()}' for elemento in lista
}
print(dicionario)
print()

import locale
print('Interar sobre um outro dicionário atravéz do método itens')
# Configura o locale pra Português do Brasil (pt_BR)
locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')

carros_esportivos = {  
  'ferrari': 1299000,
  'lamborghini': 1100000,
  'porsche': 759000
}

dict_saida = {
  chave: f'{chave.upper()}: {locale.currency(valor)}' for chave, valor in carros_esportivos.items()
}

print(dict_saida)
print()

# Configura o locale pra Português do Brasil (pt_BR)
locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')

carros_esportivos = {  
  'ferrari': 1299000,
  'lamborghini': 1100000,
  'porsche': 759000
}
#{chave if condicao: valor for elemento in iteravel}
dict_saida = {
  chave: f'{chave.upper()}: {locale.currency(valor)}' 
  for chave, valor in carros_esportivos.items() if valor > 1000000
}

print(dict_saida)
print()

print('Iterando sobre vários if')
# Configura o locale pra Português do Brasil (pt_BR)
locale.setlocale(locale.LC_MONETARY, 'pt_BR.utf8')

carros_esportivos = {  
  'ferrari': 1299000,
  'lamborghini': 1100000,
  'porsche': 759000
}
'''
Chave será f'{chave}-valor-abaixo' caso valor seja menor que 1000000.
Valor será f'{chave.upper()}: Valor abaixo de R$ 1.000.000,00' caso valor seja menor que 1000000.
'''

dict_saida = {
  chave if valor > 1000000 else f'{chave}-valor-abaixo':
    f'{chave.upper()}: {locale.currency(valor)}' 
    if valor > 1000000 else f'{chave.upper()}: Valor abaixo de R$ 1.000.000,00'
  for chave, valor in carros_esportivos.items()
}