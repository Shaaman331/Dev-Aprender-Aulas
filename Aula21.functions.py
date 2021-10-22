'''
FUNÇÕES PYTHON
* Uma função é um bloco de código que só é executado quando é chamado.
Você pode passar dados, conhecidos como parâmetros, para uma função.
Uma função pode retornar dados como resultado. 

Criação de uma função
* Em Python, uma função é definida usando o def palavra-chave: 

Chamando uma função
* Para chamar uma função, use o nome da função seguido por parênteses: 

Argumentos

* As informações podem ser passadas para funções como argumentos.
Os argumentos são especificados após o nome da função, entre parênteses. 
Você pode adicionar quantos argumentos quiser, apenas separe-os com uma vírgula.

* O exemplo a seguir tem uma função com um argumento (fname). 
Quando a função é chamada, passamos um primeiro nome, que é usado dentro 
da função para imprimir o nome completo: 

'''
print('Criando uma função')
def my_function():
  print("Hello from a function") 
print()

print('Chamando uma função')
def my_function():
  print("Hello from a function")

my_function()
print()

print('Argumentos')
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") 
print()

print('Usuário e senha')
def Logar(usuario, senha):
    print(f'logando com o usuário{usuario}')
    print(f'logando com a senha{senha}')

Logar('Tarcisio','12323232')
print()
'''
Você vai criar um função que recebe seu nome e endereço como parâmetro e depois
imprime na tela seu nome e endereço usando os argumentos que você passou para ela
'''

print('Nome e endereço')
def Cadastro(nome, endereco):
    print(f'Cadastrando nome do usuário: {nome}')
    print(f'Cadastrando endereço do usuário: {endereco}')

Cadastro('Lucca','Estrada do Portela 662 - Madureira')
print()

