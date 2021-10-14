''' 
Python: Estrutura condicional if-else
* Quando programamos, muitas vezes precisamos que determinado bloco de código seja executado apenas se uma 
determinada condição for verdadeira. Em casos assim, devemos fazer uso de uma estrutura de condição.

if 
* O if é uma estrutura de condição que permite avaliar uma expressão e, de acordo com seu resultado,
 executar uma determinada ação.

* Como podemos notar, essa estrutura é formada pela palavra reservada if, seguida por uma condição e por dois 
pontos (:). As linhas abaixo dela formam o bloco de instruções que serão executadas se a condição for atendida. 

if-else
* No entanto,se nenhum comportamento específico foi definido para o caso de a condição não ser satisfeita. 
Quando isso é necessário, precisamos utilizar a reservada else.

* Dessa vez, caso a condição avaliada na linha 3 não seja atendida, definimos o fluxo alternativo que o código 
deve seguir. Ou seja, se a idade não for maior ou igual a 18, o bloco abaixo da palavra reservada else deverá 
ser executado.

if-elif-else
* Se existir mais de uma condição alternativa que precisa ser verificada, devemos utilizar o elif para avaliar as 
expressões intermediárias antes de usar o else,

* Na linha 2 definimos a primeira condição (idade < 12). Caso essa não seja atendida, o programa seguirá para a 
linha 4 e avaliará a próxima condição (elif), que se for verdadeira fará com que o bloco logo abaixo 
(a linha 5, nesse caso) seja executado. Caso essa condição ainda não seja atendida (elif), há uma outra 
alternativa na linha 6 que será avaliada e que fará com que o bloco logo abaixo seja executado se ela for 
atendida. 
Por fim, se nenhuma das condições for satisfeita, o programa seguirá para a linha 8, executando o que é definido 
pelo else.
'''
print('Executando if')
idade = 18
if idade < 20:
    print('Você é jovem!')
print()

print('Executando if-else')
idade = 18
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
print()

print('Executando if-elif-else')
idade = 18
if idade < 12:
    print('crianca')
elif idade < 18:
    print('adolescente')
elif idade < 60:
    print('adulto')
else:
    print('idoso')
print()

print('Horário de funcionamento da loja')
horario_de_chegada = 6

if horario_de_chegada < 8:
    print('A loja ainda não abriu')
elif horario_de_chegada > 18:
    print('A loja já fechou ')
else:
    print('Volte no horário comercial')
print()

print('Cenário mais realista')
if horario_de_chegada >= 8 and horario_de_chegada <=12:
    print('A loja está aberta')
elif horario_de_chegada >= 14 and horario_de_chegada <= 18:
    print('A loja está aberta')
else:
    print('A loja está fechada')
