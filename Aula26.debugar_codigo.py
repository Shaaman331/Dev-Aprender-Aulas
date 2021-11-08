'''
Depuração 
* É uma técnica de programação em que é possível manipular a execução de cada linha e verificar os valores 
das variáveis (instâncias).

* É correto dizer que depurar um código significa a execução de cada linha vagarosamente, onde o programador 
é quem diz quando que determinada instrução deve ser executada. 
E também, a cada linha executada, é possível verificar o valor das variáveis que estão no escopo local e global

* A depuração é comumente utilizada para na detecção de erros e para entender o estado do programa e de suas 
variáveis num determinado instânte, ou numa determinada função.

* Podemos dizer que é possível depurar qualquer código de qualquer linguagem, até porque, esse é um recurso 
atualmente considerado elementar para a correta construção de software

O RECURSO DE DEPURAÇÃO
* A depuração é um recurso disponibilizado pelo compilador ou interpretador da linguagem. Portanto, nativamente, 
conseguimos depurar o código através da linha de comando, semelhate a forma como executamos o código.

* As IDE ao implementarem os recursos de depuração estão de fato negociando com o compilador ou interpretador o 
local em que deve haver interrupções e todos os demais recursos.

* É importante sabermos que não são as IDE que implementam a capacidade de depurar o código, elas apenas dialogam 
com o compilador ou interpretador e fornecem uma forma gráfica para depuração.

PRIMÓRDIOS DA DEPURAÇÃO
* Todas as vezes em que utilizamos a função print() para enviar à saída padrão o valor de variáveis estamos depurando 
nosso código de forma primitiva. Ou seja, estamos inspecionando o valor das variáveis e o estado do programa utilizando 
a função print.

O QUE SIGNIFICA CURSOR DE EXECUÇÃO?
* Cursor de execução é o termo que utilizamos para nos referirmos a linha de código em que estamos, ou melhor, 
na linha onde estamos.

O QUE SIGNIFICA breakpoint?
* A palavra breakpoint, significa, na depuração de programas, o número da linha em que a execução do código será 
interrompido para o início da depuração.

* Esse é um recurso permite interrompermos a execução do nosso programa num determinado ponto. Assim, podemos marcar 
em qual local do programa desejamos iniciar a depuração e quando o cursor de execução chegar na linha demarcada, 
a execução será interrompida e a IDE trará o código em que ocorreu a interrupção

A DEPURAÇÃO COMO ESTUDO
* A depuração deve ser utilizada durante toda a fase de estudo e, posteriormente, quando desejarmos entender como 
o interpretador do Python está lidando com determinada situação.

'''
import random


class EmailBoasVindas:
    def __init__(self):
        self.pessoas = ['Cristiam','Robert','Ana']

    def Iniciar(self):
        print('Olá bem vindo a este site!')
        self.ChutarIdade(self.pessoas)
        self.ChutarNome()
        self.ChutarCor()
        print('Programa finalizado')
    
    def ChutarCor(self):
        cores = ['azul','rosa','verde']
        for cor in cores:
            print(f'As opções de cores são: {cor}')
        
        print('Sua cor favorita é:')
        cor_preferida = random.choice(cores)
        print(cor_preferida)

    def ChutarNome(self):
        nome = f'Bem vindo: {random.choice(self.pessoas)}'
        print(nome)
    
    def ChutarIdade(self,pessoas):
        idade = f'Sua idade é: {random.randint(10,50)}'
        print(idade)

email = EmailBoasVindas()
email.Iniciar()
