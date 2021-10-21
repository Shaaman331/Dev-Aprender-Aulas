'''
Python tem dois comandos de loop primitivos:

    while loops
    for loops

Com o while loop podemos executar um conjunto de instruções enquanto uma condição 
for verdadeira. 

A instrução while funciona assim:
Assim que começa o while, ele faz um teste (como se fosse um IF teste condicional) e testa a instrução <teste>.

Se este teste resultar em verdadeiro (TRUE), tudo que está dentro do laço while (codigo1, codigo2, codigo3..., 
é executado).

Terminou de executar tudo?
Testa de novo. Deu true? Executa tudo de novo...

E fica assim, testando, executando, testando, executando...
Como se fosse um looping. E, de fato, é um looping.

E só vai parar quando o teste for FALSE.
Aí acaba o while e o 'codigo4', de fora, é executado e o script segue seu percurso naturalmente.

'''
'''print('Laço While')
i = 1
while i <=6:
  print(i)
  i += 1'''

'''print('Percorrer preço celular')
preco_celular = 10
while preco_celular <= 10:
    print('Verificando se o preço do celular mudou')
print(f'Preço do celular mudou para: {preco_celular}')
print()'''


'''print('Percorrer mais sites')
percorrer_mais_sites = True

while percorrer_mais_sites == True:
    print('Percorrendo  sites')
    percorrer_mais_sites = False
print()
'''
'''
CONTADOR

Primeiro definimos nossa variável com valor 1.
Depois testamos se ela é menor que 10. Como é, vai executar o laço while.
Primeiro, imprime o valor da variável, que é 1.
Depois adiciona 1 a essa variável.

Agora ela vale 2. O teste é realizado, como 2 é menor que 10.
Executa de novo...imprime 2, incrementa e agora a variável é 3.

E assim vai indo, indo, repetindo, repetindo...vai chegar uma hora que 'numero=10'

Como 'numero<=10' é verdadeiro, o laço while é executado.
O número 10 é impresso na tela, e ele vira 11.

Agora, o teste vai dar falso e o while vai parar de executar.
E prontinho, você imprimiu do número 1 até o 10 usando o laço while!
'''

print('Contador até 10')
numero=1

while numero<=10:
    print(numero)
    numero += 1
print()

'''
Exemplo 2 de uso do laço WHILE

"Faça um programa que peça um número maior que 1 ao usuário. 
Em seguida, imprima todos os números, de 1 até o número que o usuário informou".

'''
print('Contador 2')
print()

numero=1
max = int(input("Digite um inteiro maior que 1: ") )

while numero <= max: #O valor vai ser informado pelo usuário, sera armazenado essa informação na variável 'max' (de máximo).
    print(numero)
    numero += 1
print()

'''
 Exemplo 4 de uso do laço WHILE

"Crie um programa que peça um número ao usuário e imprima todos os números pares de 1 até o número fornecido"

Vamos usar o código do exemplo 2.
Porém, não vamos sair imprimindo tudo. Devemos fazer um teste antes (teste condicional IF) para saber se o número 
é primo, se for aí sim imprimimos.

Ou seja, vamos ter um IF dentro de um WHILE:
'''
print('Imprima todos os números pares')
numero=1
max = int(input("Digite um inteiro maior que 1: ") )

print("Numeros pares entre 1 e", max, ":") #Informa todos os valores até o (max) fornecidos

while numero <= max:
    if numero%2==0: #Devemos fazer um teste antes (teste condicional IF) para saber se o número é primo, se for aí sim imprimimos.
        print(numero,  end=" ") #end=" " é para mostrar um espaço em branco após imprimir cada número, ao invés de quebra de linha (enter).
    numero+=1

print()
'''
 Exemplo 5 de uso do laço WHILE
"Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha"

Obviamente, a senha é o número mais importante do universo:
senha='2112'

A senha que o usuário vai digitar, vai ficar na variável 'tentativa'.

Se 'senha' e 'tentativa' forem diferentes, o laço while fica repetindo e repetindo e repetindo...
sempre pedindo a senha ao usuário.

O laço while só acaba quando as variáveis 'senha' e 'tentativa' forem iguais, ou seja, quando o usuário digitar 
a senha correta:

'''
print()
print('Digitador de senha')
senha='2112'
tentativa=input("Digite a senha:")

while (senha != tentativa): #Se senha for  diferente
    print("Senha errada! Tente novamente!")
    tentativa=input("Digite a senha:") #Se senha for igual

print("Senha correta. Entrando no sistema...") 
print()

'''
 Exemplo 6 de uso do laço WHILE

"Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha, 
seu único script serve para todos os casos"

Primeiro, perguntamos quantos alunos tem na turma e armazenamos em "alunos".

* Vamos usar uma variável de apoio, chamada 'count', ela vai de 1 até o número de alunos, ok ? 
Ela que é incrementada no laço while (cresce de um em um).

* A soma de todos os alunos, armazenamos na variável 'soma'.

Agora vem o laço while.
* O teste é se 'count' é menor que 'alunos'. Se sim, vamos pedir a nota de cada aluno, do primeiro até 
o aluno de número 'alunos'.

* A nota que o usuário digitar, vai ser armazenada na variável 'nota'.
Em seguida, armazenamos na variável 'soma'.

* E assim vai indo, de aluno em aluno...no final, temos a soma total das notas de todo mundo, 
e não importa o número de alunos na turma, seja um aluno, 10, 20 ou mil alunos, a variável 'soma' vai ter 
a soma da nota de todo mundo.

* Quando acabar o while basta dividir essa 'soma' pelo número de alunos ('alunos') e prontinho, 
temos a média da turma, não importando o tamanho da turma:

'''

print('Programe um script que calcule a média da turma, não importao número de alunos que ela tenha.')

alunos=int(input("Numeros de alunos na turma: "))

count=1; soma = 0.0 #Incrementa no laço 
while count <= alunos: #Teste se count é menor que alunos
    print("Nota do aluno ", count, ":") #Pede nota do aluno do primeiro até numero de alunos
    nota = float( input() ) #Armazenar a nota que o usuário vai digitar
    soma += nota # Armazena em seguida na váriavel soma
    count += 1 # Vai testando de aluno em aluno

print("Media da turma: ", (soma/alunos) ) #Divede "soma" pelo néumero de "alunos"
