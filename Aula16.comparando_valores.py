'''
Operador 	Nome 	            Função
== 	        Igual a 	        Verifica se um valor é igual ao outro
!= 	        Diferente de        Verifica se um valor é diferente ao outro
> 	        Maior que 	        Verifica se um valor é maior que outro
>= 	        Maior ou igual 	    Verifica se um valor é maior ou igual ao outro
< 	        Menor que 	        Verifica se um valor é menor que outro
<= 	        Menor ou igual 	    Verifica se um valor é menor ou igual ao outro

Operadores Lógicos
*Esses Operadores nos possibilitam construir um tipo de teste muito útil e muito utilizado em qualquer 
programa Python: os testes lógicos.
* Python nos disponibiliza três tipos de Operadores Lógicos: o and, o or e o not.

Operador 	Definição
and 	    Retorna True se ambas as afirmações forem verdadeiras
or 	        Retorna True se uma das afirmações for verdadeira
not 	    retorna Falso se o resultado for verdadeiro

Operadores de Identidade
* Estes Operadores são utilizados para comparar objetos, verificando se os objetos testados referenciam o 
mesmo objeto (is) ou não (is not).

Operador 	Definição
is 	        Retorna True se ambas as variáveis são o mesmo objeto
is not 	    Retorna True se ambas as variáveis não forem o mesmo objeto

* Muitas vezes programadores Python ficam na dúvida em quando utilizar o operador de igualdade == ou 
o operador de identidade is.

* Mas agora que você já conhece os dois sabe que o operador == verifica os valores testados, 
enquanto o operador is testa a referência dos valores testados! 

Operadores de Associação
* Eles servem para verificar se determinado objeto está associado ou pertence a determinada estrutura de dados.

Operador 	Função
in 	        Retorna True caso o valor seja encontrado na sequência
not in 	    Retorna True caso o valor não seja encontrado na sequência
'''
a =50  
b = 5
print(a > b)
print()


print(a >= b)
print()

print(a == b)
print()

print(a != b)
print()

x = a == b and 'ola' == 'ola'
print(x)
print()

print('Operadores de Comparação')
var = 5

if var == 5:
    print(f'Os valores de {var} são iguais')

if var != 7:
    print(f'O valor de {var} não é igual a 7')

if var > 2:
    print(f'O valor da variável {var} é maior de 2')

if var >= 5:
    print(f'O valor da variável {var} é maior ou igual a 5')

if var < 7:
    print(f'O valor da variável {var} é menor que 7')

if var <= 5:
    print(f'O valor da variável {var} é menor ou igual a 5')

print()

print('Operadores Lógicos')
num1 = 7
num2 = 4

# Exemplo and
if num1 > 3 and num2 < 8:
    print("As Duas condições são verdadeiras")

# Exemplo or
if num1 > 4 or num2 <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Exemplo not
if not (num1 < 30 and num2 < 8):
    print('Inverte o resultado da condição entre os parânteses')

print()

print('Operadores de indentidade')
lista = [1, 2, 3]
outra_lista = [1, 2, 3]
recebe_lista = lista
print('Exemplo operador is:')
# Recebe True, pois são o mesmo objeto
print(f"São o mesmo objeto? {lista is recebe_lista}")

# Retorna False, pois são objetos diferentes
print(f"São o mesmo objeto? {lista is outra_lista}")
print()

print('Exemplo operdaro is not')
tupla = (1, 2, 3)
outra_tupla = (1, 2, 3)

print(f"Os objetos são diferentes? {outra_tupla is tupla}")
print()

print('Operadores de asssociação')
print('Exemplo operadores in  e not in')
lista = ["Python", 'Academy', "Operadores", 'Condições']

# Verifica se existe a string dentro da lista
print('Python' in lista)  # Saída: True

# Verifica se não existe a string dentro da lista
print('SQL' not in lista) # Saída: True
