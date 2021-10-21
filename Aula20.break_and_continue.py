'''
Break e Continue

A declaração break
* Com a break instrução , podemos parar o loop mesmo se o enquanto a condição for verdadeira: 
 
Instrução BREAK em Python
Um comando muito importante e usado em laços Python, é o BREAK, que significa 'quebrar', 'interromper', 'pausar'. 
E é isso que faz.

while TESTE:
    codigo
    if TESTE2:
       break;
    ...
A função do BREAK é simplesmente parar o looping.
Se fizer um teste, ele der positivo e você usar a break, o laço é automaticamente findado.

A declaração continue
* Com a continue instrução , podemos parar o iteração atual e continue com a próxima: 

Instrução CONTINUE em Python
* Na instrução BREAK, quando ela é executada, tudo para, tudo acaba, adeus laço, adeus WHILE, adeus FOR, 
termina ele.

* Se ao invés de break usar continue, o laço não é terminado. 
Porém, ele pula do continue pro início do laço, tudo que tem ali em diante do continue não é mais executado.


'''
print('Instrução Break')
estilos_musicais = ['rock', 'pop', 'samba', 'eletronica']
for estilo in estilos_musicais:
    if estilo == 'eletronica':
        break
    print(estilo)
print()

print('Instrução Continue')
estilos_musicais = ['rock','pop', 'samba','eletronica']
for estilo in estilos_musicais:
    if estilo == 'rock':
        continue
    print(estilo)
print()

print('Sai do loop quando i for 3')
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 
print()

print('Contnue para a próxima interação se i for 3')
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print()
'''
A soma total ficará armazenada em total.
Vamos percorrer todos os números de 1 até 1 milhão, quem vai assumir todos esses valores é a variável count, nosso contador.

Primeiro incrementamos nosso contador. Ele começa em 0 e logo vira 1.
Agora, vamos fazer um teste para saber se o valor de count é múltiplo de 3.

Se for múltiplo de 3, damos uma instrução continue e o loop for segue para o próximo elemento, nada é feito, 
pulamos para a próxima iteração.

Caso não seja múltiplo de 3, vamos somar esse valor do contador na variável total.
'''
print('Escreva um programa que vai somar todos os números até 10000 menos os multiplos de 3')
total=0 #A soma fica armazenada em total

for count in range(10000):
    count += 1 #Incrementamos nosso contador, começa em 0 e vira 1
    if(count % 3 == 0 ): continue # Teste para saber se count é multiplo de 3
    total += count #Caso não seja multiplo de 3, vamos somar valor do contador na variável total
    
print(total) 


