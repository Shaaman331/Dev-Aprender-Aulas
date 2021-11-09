'''
Função map() Python
* A função map() executa uma determinada função para cada item em um iterável. 
O item é enviado para a função como um parâmetro.

Sintaxe
map(funções, iteráveis)

Valores de Parâmetro 
Parametros   Descrição
funções      Obrigatório. A função a ser executada para cada item
iteráveis    Obrigatório. Uma sequência, coleção ou objeto iterador. 
             Você pode enviar quantos iteráveis ​​desejar, apenas certifique-se 
             de que a função tenha um parâmetro para cada iterável.
'''
print('Iterando atráves da função range')
numeros = []
for i in range(5):
    numeros.append(i)
print(numeros)
print()
#Map
print('Interando atráves de funções')
nomes = ['Lucca','Marco','Raquel','John']
def aprovar_pessoa(nome):
    return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))
print()

print('Iterando atráves de funções')
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry')) 
print()

print('Concatenando lista')
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')) 
