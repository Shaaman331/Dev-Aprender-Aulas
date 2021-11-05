'''
Tratamento de erros(try except)
* O bloco try permite que você teste um bloco de código para erros.
* O bloco except permite que você lidar com o erro.
* O bloco finaly permite que você executa o código, independentemente do resultado dos blocos try- e except

Manipulação de exceção
* Quando ocorre um erro, ou exceção, como a chamamos, o Python normalmente para e gerar uma mensagem de erro.
* Essas exceções podem ser tratadas usando o try  
* Visto que o bloco try levanta um erro, o bloco except será executado.
* Sem o bloco try, o programa irá travar e gerar um erro

Muitas exceções
* Você pode definir quantos blocos de exceção quiser, por exemplo, se quiser executar um bloco especial de 
código para um tipo especial de erro:  

Else
* Você pode usar o else palavra-chave para definir um bloco de código a ser executado se nenhum erro for levantado: 

Finalmente

O bloco finally, se especificado, será executado independentemente se o bloco try levanta um erro ou não.
Isso pode ser útil para fechar objetos e limpar recursos: 

'''
print('Teste de erros ')
#O bloco try irá gerar uma exceção, Porque x não está definido:
try:
  print(x)
except: #O bloco except permite você lidar com o erro 
  print("An exception occurred")
print()

print('Teste 2 -Erro de input')
try: # Testa o bloco para erros
    ano_atual = int(input('Qual é o ano atual ?'))
except ValueError: # Permite que você lide com erros
    print('Vocẽ deve digitar um número')
print()

print('Teste 2 - Erro de divisão')
try: #Testa o bloco para erros
    print(5/0)
except ZeroDivisionError: #Permite lidar com erros de divisão
    print('Não é possivel dividir por 0')
print()

print('Teste 3 - Erro de divisão')
try: #Testa o bloco para erros
    print(5/0)
except: #Permite que vocẽ lide com erros
    print('Ocorreu um erro')
finally: #Permite você executar o código, independente do resultado dos blocos
    print('O usuário X realizou calculos no sistema') 
print()

print('Teste 4 função range')
for pagina in range(10): #Percore uma lista usando a função range
    try: #Testando o bloco para erros
        print('Buscando informações') #Exibe 10X buscando informações no laço
        print(5/0) #Error
    except: #Permite que vocẽ lide com erros
        pass  #Continua rodando mesmo encontrando excessão
print()

print('Teste 5 - Mulplas exceções, isso pode ser útil para fechar objetos e limpar recursos: ')
try: #Testando o bloco para erros
  print(x) #Error 
except NameError: #Exceção de erros de nome
  print("Variable x is not defined")
except: #Permite que você lide com erros
  print("Something else went wrong") 
print()

print('Teste 6 - usando else, neste exemplo, o bloco try não gerar qualquer erro: ')
try: #Testando o bloco para erros
  print("Hello") 
except: #Permite que vocẽ lide com erros
  print("Something went wrong")
else: #Define bloco para ser executado sem nenhum erro
  print("Nothing went wrong") 
print()

print('Usando file para tratar abertura de arquivos')
try: #Testando o bloco para erros
  f = open("demofile.txt") #Abrir arquivo "demofile.txt"
  try: #Testando bloco para erros
    f.write("Lorum Ipsum") 
  except:#Permite que você lide com erros
    print("Something went wrong when writing to the file")
  finally:#Permite que vocẽ execute o código independe do resultado dos blocos
    f.close() #Fecha arquivo 
except:
  print("Something went wrong when opening the file") 
