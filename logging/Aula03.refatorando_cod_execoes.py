'''
Exceptions
'''
import logging #Importando Módulo

logging.basicConfig( #Fornecendo o nivel usado
    filename="info1.log", #Especifica o arquivo onde as informações devem ser armazenadas
    level=logging.DEBUG, #Especifica o nivel da gravidade difinada pela raiz
    format="%(levelname)s %(asctime)s : %(message)s", #Define o formato que a menssagem de log é inserida no arquivo
    datefmt = "%d/%m/%Y %H:%M:%S", #Define o formato de data e hora
)
logger = logging.StreamHandler() #Cria instancia de gerenciamento
logging.getLogger('').addHandler(logger) #Cria instancia e usa para chamar o logger

try: #Testando o bloco para erros
    ano_atual = int(input('Qual é o ano atual? '))
except ValueError: #Permite que você lide com erros
    logging.warning('Você deve digitar um número.') #Usando objeto para chamar a função warning
print()

print('Testando ZeroDivisionError')
try:
    print(5/0)
except ZeroDivisionError:
    logging.warning('Não é possivel dividir por 0')
print()

print('Testando Divisão por 0')
try:
    print(5/0)
except:
    logging.warning('Ocorreu um erro')
print()


print('Testando o finally')
try:
    print(5/0)
except:
    logging.warning('Ocorreu um erro')
finally:
    logging.info('O usuário x realizou calculos no sistema')

