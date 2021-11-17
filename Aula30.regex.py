'''
Python RegEx 
* Um RegEx, ou Expressão Regular, é uma sequência de caracteres que forma um padrão de pesquisa.
* RegEx pode ser usado para verificar se uma string contém o padrão de pesquisa especificado. 

Módulo RegEx
* Python tem um pacote embutido chamado re, que pode ser usado para trabalhar com Expressões regulares.

Importe o remódulo: 

Funções RegEx
* O remódulo oferece um conjunto de funções que permite para procurar uma string para uma correspondência: 

Function 	Description
findall     Retorna uma lista contendo todas as correspondências
search      Retorna um objeto Match se houver uma correspondência em qualquer lugar da string
split       Retorna uma lista onde a string foi dividida em cada partida
sub         Substitui uma ou mais correspondências por uma string

Objeto de correspondência

* Um Match Object é um objeto que contém informações sobre a pesquisa e o resultado.
* Se não houver correspondência, o valor Nonevai ser retornado, em vez de Match Object.


O objeto Match possui propriedades e métodos usados ​​para recuperar informações sobre a pesquisa e o resultado:

.span()retorna uma tupla contendo as posições inicial e final da correspondência.
.stringretorna a string passada para a função
.group()retorna a parte da string onde havia uma correspondência 

'''
import re

hey = 'carol@gmail.com.br'

#Findall 
print('A função findall')
result = re.findall(r"(@.{1,8}\.)",hey)
print(result)
print()
#Search busca em formma de objeto
print('A função search')
result = re.search(r"(@.{1,8}\.)",hey)
print(result)
print()

#Split busca por parte
print('A função split')
result = re.split(r"(@.{1,8}\.)",hey)
print(result)
print()
#Sub 
print('A função sub')
result = re.sub(r"(@.{1,8}\.)",'@yahoo.',hey)
print(result)
print()

print('A função findall')
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#A lista contém as correspondências na ordem em que são encontradas.
#Se nenhuma correspondência for encontrada, uma lista vazia será retornada: 
print('A função findall')
print('Retorna uma lista contendo todas as correspondências.')
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) 
print()

#O search()função procura a string para uma correspondência e retorna um objeto Match se houver um partida.
#Se houver mais de uma correspondência, apenas a primeira ocorrência da correspondência será retornada: 
print('A função search')
print('Procure o primeiro caractere de espaço em branco na string: Search')
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 
print()

print('A função Search')
print('Faça uma pesquisa que não retorne nenhuma correspondência:') 
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) 
print()

print('A função split retorna uma lista onde a string foi dividida em cada partida')
print('Dividido em cada caractere de espaço em branco:')
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) 
print()

print('Divida a string apenas na primeira ocorrência:')
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 
print()

print('A função sub substitui as correspondências com o texto de sua escolha:')
print('Substitua cada caractere de espaço em branco pelo número 9:')

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) 
print()



print('Você pode controlar o número de substituições, especificando o count parâmetro:')
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) 
print()

print('Faça uma pesquisa que retornará um Match Object:')
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object 
print()

print('Imprime a posição (posição inicial e final) da primeira ocorrência de correspondência.')
print('A expressão regular procura por qualquer palavra que comece com maiúscula "S":')
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print()

print('Imprima a string passada para a função:')
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) 
print()

print('A expressão regular procura por qualquer palavra que comece com maiúscula "S":')
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) 
print()
