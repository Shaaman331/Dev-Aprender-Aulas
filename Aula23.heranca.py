'''
Herança Python
* A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.
* A classe pai é a classe da qual está sendo herdada, também chamada de classe base.
* A classe filha é a classe que herda de outra classe, também chamada de classe derivada. 

Exemplo
Crie uma classe chamada Person, com firstnamee lastnamepropriedades, e um printnamemétodo: 
'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 
print()

'''
Primeiro vamos criar a classe Veiculo, que tem os atributos tipo (carro, moto, suv etc), 
modelo (celta, palio, honda, biz etc) e km que indica a quilometragem do veículo.

Agora vamos a classe Carro, que vai herdar a classe Veiculo.
Ela recebe os atributos tipo, modelo, km e o portas.

Como os três primeiros são da classe base, a Veiculo, basta chamarmos o método __init__ 
da classe Veiculo passando tais argumentos.

O único parâmetro novo é o portas, pois Carro tem porta, mas nem todo Veiculo tem porta.
Criamos também um novo método, o exibe(), que vai exibir os dados do carro. 
'''
class Veiculo: #Criando classe Veiculo
 def __init__(self, tipo, modelo, km): #Craindo atributos 
  self.tipo = tipo #objetos
  self.modelo = modelo #objetos
  self.km = km #objetos

class Carro (Veiculo): #Criando classe Carro que vai herda a classe Veiculo
 def __init__(self, tipo, modelo, km, portas): #Criando atributos herdados
  Veiculo.__init__(self, tipo, modelo, km) #Acessamdo o método __init__ herdadando os argumentos
  self.portas = portas # Criando parametro novo
 
 def exibe(self): #Criar metodo para exibir dados dos carros
  print(self.tipo, "modelo", self.modelo, "com", self.km, 
     "km rodados e", self.portas, "portas.")
  
palio = Carro("Carro", "Palio", "10000", 2) #Acessando a classe Carro
palio.exibe() #Acessaando metodo exibir

class Moto(Veiculo): #Craindo classe filho Moto(Veiculo):
  def __init__(self, tipo, modelo, km, cilindradas):#Acessando atributos herdados 
      super().__init__(tipo, modelo, km)
      self.cilindradas = cilindradas #Novo parametro

  def exibe(self): #Criando método exibe novas informações
      print(self.tipo, "modelo", self.modelo, "com", self.km, "km rodadados e", self.cilindradas, "cilindradas") #Exibindo novas informações

honda_xtz = Moto("Moto", "Honda xtz","35000",300) #Acesasando a classe Moto 
honda_xtz.exibe() # Acessando método exibe
print()

print('Criando classe Computador')

class Computador: #Criando classe Computador
  def __init__(self, marca, memoria_ram, placa_de_video): #Criando atributos
    self.marca = marca #objetos
    self.memoria_ram = memoria_ram #objetos
    self.placa_de_video = placa_de_video #objetos

  def Ligar(self):#Criando método Ligar
    print('Ligando computador')

  def Desligar(self): #Criando método Desligar
    print('Desligando computador')

  def InformacaoComputador(self): #Criando método InformaçãoComputador
    print(self.marca, self.memoria_ram, self.placa_de_video)
    
class ComputadorGamer(Computador): #Criando classe filho ComputadorGamer
  def __init__(self, marca, memoria_ram, placa_de_video, tamanha_da_torre):#Acessando atributos herdados
      super().__init__(marca, memoria_ram, placa_de_video)
      self.tamanho_da_torre = tamanha_da_torre #Criando novo parametro

  def InformacaoComputador(self): #Criando método para exibir novas informações
      print(self.marca, self.memoria_ram, self.placa_de_video, self.tamanho_da_torre) #Exbindo novas informaçõss

  def trocar_cor_led(self, cor):#Criando método trocar_cor_led
    print(f'Trocando cor dos led para {cor}') #Recebendo funcionabilidade
  
  def ligar_ventoinha(self): #Criando método ligar_ventoinha
    print('Ligando ventoinha')
  
  def desligar_ventoinha(self):#Criando método desligar_ventoinha
    print('Desligando ventoinha')

pc_gamer = ComputadorGamer('Asus', '16gb', 'Nvidea 1080TI', 'Médio') #Criando classe pc_gamer chamando a classe ComputadorGamer
pc_gamer.Ligar() #Acessando métodos Ligar 
pc_gamer.InformacaoComputador() #Acessando método InformacaoComputador
pc_gamer.trocar_cor_led('Azul') #Acessando método trocar_cor_led
pc_gamer.ligar_ventoinha() #Acessando método ligar_ventoinha
pc_gamer.desligar_ventoinha() #Acessando método desligar_vetoinha
print()
''''
Crie uma classe chamada NavegadoresSites:
Esta classe terá duas propiedades "site", "conteudo_de_busca"
A classe terá também um método chamado:
"acessar_site", esse método deverá imprimir qual site esta navegando 
e qual informação será extraida, com bases nas informações que foram passadas no contrutor.
Agora você irá criar novas funcionabilidades especifícas
para um tipo de site de comparação de produtos como o MercadoLivre, então
vamos manter as informações para qual site devemos navegar e qual informação deve ser extraida.
Você pode chamar essa classe de "NavegadoSiteComparacao"
Ele deve conter um método adicional que é chamado de "buscador_de_preco", esse método deve 
receber o "nome do produto" ele deve buscar e também o "preço", que irá representar o valor 
máximo que você está disposto a pagar
'''
print('Navegador de sites')

class NavegadorSites:
  def __init__(self, site, conteudo_de_busca):
    self.site = site
    self.conteudo_de_busca = conteudo_de_busca

  def acessar_site(self):
    print(
      f'Navegando até  o site {self.site} para estrair {self.conteudo_de_busca}'
    )

class NavegadorSiteComparacao(NavegadorSites):
  def buscador_de_preco(self, nome_do_produto, preco):
    print(
      f'Buscando informações sobre {nome_do_produto} com preço máximo de {preco}'
    )

     
navegador = NavegadorSiteComparacao('https://www.olox.com', 'relógios')
navegador.acessar_site()
navegador.buscador_de_preco('Relogio digital ',400)
