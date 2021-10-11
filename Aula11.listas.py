''''
Lista
* As listas são usadas para armazenar vários itens em uma única variável.

* Listas são um dos 4 tipos de dados integrados em Python usados ​​para armazenar 
coleções de dados, os outros 3 são tupla , Conjunto e Dicionário , todos com diferentes 
qualidades e usos.

* As listas são criadas usando colchetes: 

Lista de itens
* Os itens da lista são ordenados, alteráveis ​​e permitem valores duplicados.

* Os itens da lista são indexados, o primeiro item tem índice [0], o segundo item tem índice [1] etc. 

Ordenado
* Quando dizemos que as listas estão ordenadas, significa que os itens têm uma ordem definida e essa 
ordem não mudará.

* Se você adicionar novos itens a uma lista, os novos itens serão colocados no final da lista. 

Mutável

* A lista pode ser alterada, o que significa que podemos alterar, adicionar e remover itens de uma lista após sua criação

Permitir Duplicados

* Como as listas são indexadas, elas podem ter itens com o mesmo valor: 

Comprimento da lista

* Para determinar quantos itens uma lista possui, use o len()função:

Itens de lista - tipos de dados
*Os itens da lista podem ser de qualquer tipo de dados: 


O construtor list ()
* Também é possível usar o list () construtor ao criar um nova lista. 

'''
print('Listas')
thislist = ["apple", "banana", "cherry"]
print(thislist)
print()

print('Listas permitem valores duplicados')

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
print()

print('Cumprimento de uma lista')
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
print()

print('Tipos de dados')
list1 = ["apple", "banana", "cherry"]
print(type(list1))
list2 = [1, 5, 7, 9, 3]
print(type(list2))
list3 = [True, False, False]
print(type(list3))
print()
print('Construtor list')
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print()

site1 = 'youtube.com'
site2 = 'facebook.com'
site3 = 'instagram.com'

sites = ['youtube.com', 'facebook.com','instagram.com']

print(sites[1]) #Aceesando pelo indice
sites.append('linkdin.com') #adicionando pelo append
print(sites)
sites.remove('instagram.com')
print(sites)
print()

print('Listas dinâmicas')
pessoas = [['Lucca', 3]], [['Raquel', 15]]
print(pessoas)
print(pessoas[1][0])
