'''
Tupla
* Tuplas são usadas para armazenar vários itens em uma única variável.

* Tuple é um dos 4 tipos de dados integrados em Python usados ​​para armazenar coleções de dados, 
os outros 3 são Lista , Conjunto e Dicionário , todos com diferentes qualidades e usos.

* Uma tupla é uma coleção ordenada e imutável .

* As tuplas são escritas com colchetes. 

Ordenado
* Quando dizemos que as tuplas estão ordenadas, significa que os itens têm uma ordem definida e essa ordem não mudará.

Imutável
* As tuplas são imutáveis, o que significa que não podemos mudar, adicionar ou remover itens após a tupla ter sido criada.

Permitir Duplicados
* Como as tuplas são indexadas, elas podem ter itens com o mesmo valor: 

Comprimento da Tupla
* Para determinar quantos itens uma tupla tem, use o len()função: 

Itens de tupla - Tipos de dados
* Os itens de tupla podem ser de qualquer tipo de dados: 

O construtor tupla ()
* Também é possível usar o tuple () construtor para fazer uma tupla. 

'''
print(' Tuplas')
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print()

print('Tupla com valores duplicados')
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print()

print('Itens da tupla com a função len')
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
print()

print('Tuplas tipos de dados')
tuple1 = ("apple", "banana", "cherry")
print(type(tuple1))
tuple2 = (1, 5, 7, 9, 3)
print(type(tuple2))
tuple3 = (True, False, False)
print(type(tuple3))
print()

print('Contrutor tupla')
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print('Tuplas')
site1 = 'Youtube.com'
site2 = 'facebook.com'
site1 = 'instagram.com'

valor1 = 23
valor2 = 35
valor3 = 50

sites = ('youtube.com', 'facebook.com', 'instagram.com')
valores = (23, 35 ,50)
print(sites[2])
print(valores[1])

cores_e_tamanhos = ('azul', 'verde', 'preto')+ ('alto', 'grande', 'baixo')
print(cores_e_tamanhos)

