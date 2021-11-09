''''
Listas em Python
* Lista é uma estrutura de dados provida pela própria linguagem e que utilizamos muito na programação Python.

List comprehension
* A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos 
valores de um lista existente. 
 
* Com a compreensão de lista, você pode fazer tudo isso com apenas uma linha de código: 
newlist = [expression for item in iterable if condition == True] 

Iterável
* O iterável pode ser qualquer objeto iterável, como uma lista, tupla, conjunto etc. 

List Comprehensions com if
* List comprehensions podem utilizar expressões condicionais para criar listas ou modificar listas existentes.
[expr for item in lista if cond]

Aplique a expressão expr em cada item da lista caso a condição cond seja satisfeita.

List Comprehensions com vários if’s
* Podemos verificar condições em duas listas diferentes dentro da mesma list comprehension.

List Comprehensions com if + else
* Outra forma de se utilizar expressões condicionais e list comprehension é usar o conjunto if + else.
[resultado_if if expr else resultado_else for item in lista]

* Para cada item da lista, aplique o resultado resultado_if se a expressão expr for verdadeira, caso contrário, 
aplique resultado_else.

Múltiplas List Comprehensions (aninhadas)
* Transpor uma matriz, significa transformar as linhas em colunas e vice-versa.


'''
print('List comprehension range')
nova_lista = [2 * i for i in range(10)]
#[expressão for membro in  interável]
print(nova_lista)
print()

print('List comprehension in list')
nomes = ['Lucca','Marco','Raquel','John']
#[expressão for membro in interável]
print([nome + ' APROVADO' for nome in nomes])
print()

print('List comprehesion in fuction')
def aprovar_pessoas(nome):
    return nome + ' APROVADO'

print([aprovar_pessoas(nome) for nome in nomes])
print()

print('List comprehension in matriz')
from pprint import pprint
pprint([[i for i in range(1,6)] for x in range(5)])
print()

print('Usando condicionais in list comprehesion')
nomes =['Lucca', 'Marco', 'Raquel','John']
#[expressão for membro in iterável(condicional if)]
print([aprovar_pessoas(nome) for nome in nomes if nome !='Raquel'])
print()

print('Usando funcion in list comprehesion')
def numero_par(numero):
    valor = numero % 2
    if valor == 0:
        return True
    else:
        return False

#[expressão for membro in iterável(condicional if)]
print([i for i in range(20) if numero_par(i)])
print()

#A condicional é flexível
#[expresão(condiional if) for membro in interálvel]
print('List comprehension condicional flexivel')
participantes = ['Larissa', 'Lucca','Marcos','John']
ganhadores = ['Lucca','John']
print([i +' GANHADOR' if i in ganhadores else i + ' NÃO SELECIONADO' for i in participantes])
print()

print('Desafio 1')
pprint([i *2 for i in range(1,6)])
print()

print('Desafio 2')
cores = ['vermelho', 'azul', 'verde','amarelo','rosa','preto']
# Pegamos o indice do item interado cores.index e adicionamos 1
# Convertemos toda essa expressão para uma string [str(cores.index(cor)+1)]
# Concatemos a string + '-'
# Depois iteramos i intem dentro de cores  intem"cor"
pprint([str(cores.index(cor)+1)+ '-' + cor for cor in cores])
print()
print('Desafio 3')
participantes = ['Joel','Jessica','Maria','Cris','Lucca','Marco']
pagamento_realizado = ['Joel','Jessica','Maria','Cris']
# Criamos uma condicional "i" onde vamos concatenar a paalavra "PAGO"
# Onde if condicional "i" esjeta dentro de "pagamento_realizado"
# Caso a condional "i" esteja concatemos com a palavra " PAGO" caso else concatenamos com a palavra " DEVENDO"
# Faremos isso passando todos os itens na lista de participantes "for i in participantes" 
pprint([i + ' PAGO' if i in pagamento_realizado else i + ' DEVENDO' for i in participantes])
print()

print('List comprehension  com range')
resultado = [numero for numero in range(20) if numero % 2 == 0]
#[expresão(condiional if) for membro in iterável]
print()

print('List Comprehensions com vários if’s ')
resultado = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]
#[expresão(condiional if) for membro in iterável + expressão (condicional if) in iteravél]
print(resultado)

print('List Comprehensions com if + else')
resultado = ['1' if numero % 5 == 0 else '0' for numero in range(16)]
print(resultado)

