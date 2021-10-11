'''Acessando partes de uma string

* Antes de falarmos de slicing, vamos ver rapidamente o que são as strings em Python. 
Strings em Python são objetos como outros quaisquer. Podem ser construídos com uma atribuição simples:

* Uma operação muito interessante que Python fornece para manipulação de strings é o fatiamento (slicing). 

* Fatiamento significa extrair apenas uma parte da string, ou seja, uma substring. Com essa operação, 
podemos delimitar os limites inferior e superior do pedaço da string que queremos acessar. 

* Por exemplo, se quisermos acessar a substring da posição 0 até a posição 4 na string s original, 
podemos fazer o seguinte:
'''
s = "hello, world!"
print(s.upper())

print(s.split(","))

print(s.split(",")[0])

print(s.replace("world", "dude"))
print()

print('Acessando elementos individuais de uma lista')
print (s[0])

print(s[2])

print(s[12])

'''
Para acessar o último elemento de uma string, podemos proceder de duas formas:
'''
print() 
print(s[-1])
print()

print('Fatiamento')
print(s[0:5])
print(s[:5])
print(s[2:4])
print(s[7:13])
print(s[7:])
print(s[:])
print()
print('Acessando partes de uma string')
mouse = 'Mouse'
print(mouse[1])
descricao_do_computador = 'Esse é um computador que foi lançado e chegou para revolucionar o merdaco atual'
print(descricao_do_computador[-1])
print(descricao_do_computador.index('o'))
print(descricao_do_computador.index('a'))
