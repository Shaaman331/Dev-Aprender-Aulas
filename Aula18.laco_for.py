'''
 
Estrutura de repetição for
* Em algumas situações é comum que uma mesma instrução (ou conjunto delas) precise ser executada várias vezes 
seguidas. Nesses casos, normalmente utilizamos um loop (ou laço de repetição) que permite executar o mesmo bloco 
de código enquanto uma condição é atendida. 
Em Python, os loops são codificados com as estruturas de repetição for e while.

Laço for 
* O laço for nos permite percorrer os itens de uma coleção e, para cada um deles, executar o bloco de código 
declarado no loop.

* Enquanto percorremos a lista de valores, a variável indicada no for receberá, a cada iteração, um item da 
coleção. Assim, podemos executar algum processamento com esse elemento. No código abaixo percorremos a lista 
nomes e imprimimos cada elemento.

* A variável definida na linha 1 é uma lista inicializada com uma sequência de valores do tipo string. 
A instrução for percorre todos esses elementos, um por vez e, em cada caso, atribui o valor do item à variável n, 
que é impressa em seguida. O resultado, então, é a impressão de todos os nomes contidos na lista.

For/else
* É possível adicionar a instrução else ao final do for. Isso faz com que um bloco de código seja executado ao 
final da iteração.

* Na primeira linha definimos uma variável que armazenará uma lista de nomes. Após isso, a instrução for percorre 
todos esses elementos e atribui um a um à variável n, que será impressa, como pode ser visto na linha 3. 
Após o loop se encerrar, o bloco de código contido na instrução else é acionado, imprimindo a mensagem na tela.

'''

print('Estrutura laço for')
nomes = ['Pedro', 'João', 'Leticia']
print(nomes)
for n in nomes:
     print(n)
print()

print('Estrutura laço for/else')
nomes = ['Pedro', 'João', 'Leticia']
print(nomes)
for n in nomes:
     print(n)
else:
     print("Todos os nomes foram listados com sucesso")
print()

print('Loop de fotos')
fotos = ['foto1', 'foto2','foto3', 'foto4','foto5']
for foto in fotos:
    print(foto)
print()

print('Usando a função range')
for volume in range(11): #função range roda até o penultimo número
    print(f'Aumentando o volume para {volume}')
print()

print('Especificando o valor inicial')
for volume in range(1,11): #função range roda até o penultimo número
    print(f'Aumentando o volume para {volume}')
