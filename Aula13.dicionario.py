''''
Dicionário
* Os dicionários são usados ​​para armazenar valores de dados em pares chave: valor.
* Um dicionário é uma coleção ordenada *, mutável e não permitir duplicatas. 

Itens de dicionário
* Os itens do dicionário são ordenados, alteráveis ​​e não permitem duplicatas.
* Os itens do dicionário são apresentados em pares chave: valor e podem ser referidos por usando o nome da chave. 

Ordenado ou não ordenado?
* Quando dizemos que os dicionários estão ordenados, significa que os itens têm uma ordem definida e essa ordem 
não mudará.

* Não ordenado significa que os itens não tem uma ordem definida, você não pode se referir a um item usando um
índice.

Mutável
* Os dicionários podem ser alterados, o que significa que podemos alterar, adicionar ou remover itens após o 
dicionário foi criado. 

Duplicados não permitidos
* Os dicionários não podem ter dois itens com a mesma chave: 

* Para determinar quantos itens um dicionário tem, use o len()função: 

Itens de Dicionário - Tipos de Dados
* Os valores nos itens do dicionário podem ser de qualquer tipo de dados: 

'''
print('Dicionários')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print()

print('O valor da marca:')
thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict1["brand"])
print()
print('Valores duplicados sobrescreverão os valores existentes:')
thisdict2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict2)
print() 

print('Tamanho do dicionário')
print(len(thisdict))
print(len(thisdict1))
print(len(thisdict2))
print()

print('Itens do dicionário')
thisdict4 =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} 
print(thisdict4)
print()

print('Tipo de um dicionário')
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) 
print()

print('Dicionário chave-valor')
pessoa = {'Nome':'Matheus','idade':'19', 'Altura': 168}
print(pessoa)
print()

print('Dicionário a partir de uma função')
filme = dict(nome = 'Homem-Aranha', ano_lancamento = '2000', nota = '8')
print(filme)
print()

print('Removendo valores duplicados')
nomes = ['Lucca', 'Raquel', 'Marco', 'Thiago', 'Lucca']
print(list(dict.fromkeys(nomes))) # retorna uma lista de nomes por shas chaves usando o método dict.fromkeys
