'''
Classes / objetos Python

* Python é uma linguagem de programação orientada a objetos.
A Programação Orientada a Objetos (POO) é um paradigma de programação baseado no conceito de Classes e Objetos.

Classes podem conter dados e código:
* Dados na forma de campos (também chamamos de atributos ou propriedades); e
Código, na forma de procedimentos (frequentemente conhecido como métodos).

Crie uma classe
* Para criar uma classe, use a palavra-chave class: 

Criar Objeto
* Agora podemos usar a classe chamada MyClass para criar objetos: 

* Para não esquecer mais: Classes são fôrmas de bolo e bolos são objetos
Objetos
* Objetos são instâncias de uma Classe. Objetos podem modelar entidades do mundo real (Carro, Pessoa, Usuário) 
ou entidades abstratas (Temperatura, Umidade, Medição, Configuração).


Self
* Uma importante característica dos objetos é que seus próprios métodos podem acessar e frequentemente modificar seus 
campos de dados: objetos mantém uma referência para si mesmo, o atributo self no Python.

'''
print('Classse e objetos')
class Pessoa: #Criando a classe Pessoa
    def __init__(self, nome: str, idade: int, altura: float): #Função init para atribuir valores
        self.nome = nome #self objetos
        self.idade = idade #self objetos
        self.altura = altura #self objetos
p2 = Pessoa("Tarcisio", 31, 1.72)
print(p2.nome)
print(p2.idade)
print(p2.altura)
print()

print('Crie uma classe chamada Person, use a função __init __ () para atribuir valores para nome e idade: ')
class Person:#Claase Person
  def __init__(self, name, age):#Função int para atribuir valores
    self.name = name #self objetos
    self.age = age #self objeteos

p1 = Person("John", 36) #Chando a a classe, funções "name" "age"

print(p1.name)
print(p1.age) 
print()

print('Criando classe Computador')
class Computador:
  def __init__(self,marca, memoria_ram, placa_de_video):
    self.marca = marca
    self.memoria_ram = memoria_ram
    self.placa_de_video = placa_de_video


  def Ligar(self):
    print('Ligando computador')

  def Desligar(self):
    print('Desligando computador')

  def ExibirInformacoes(self):
    print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador('Asus','16gb','Nvidea')
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInformacoes()
print()

print('Criando classe Carro')
class Carro:
  def __init__(self, marca,modelo,cor):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor


  def Ligar(self):
    print('Ligando carro')

  def Desligar(self):
    print('Desligando carro')

  def Informacoes(self):
    print(self.marca, self.modelo, self.cor)

carro1 = Carro('BMW','BMW I4 eletrico','preto')
carro1.Ligar()
carro1.Desligar()
carro1.Informacoes()
