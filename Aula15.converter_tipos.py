'''
Convertendo entre tipos 

'''
print('Convertendo para inteiro')
idade = int(input('Qual sua idade? '))
if idade >=18:
    print('Você pode entrar na festa')
else:
    print('Espere até a maior idade')
print()

print('Convertendo para float')
altura_da_parede = float(input('Qual a altura da parede? '))
print(altura_da_parede >= 2.50)
print()

print('Convertendo para lista')
modelos_de_carro = ('bmw', 'ford', 'citroen')
print(type(modelos_de_carro))
print(list(modelos_de_carro))
print()

print('Convertendo para tuplas')
cores = ['verde', 'azul', 'rosa']
print(tuple(cores))
print()

'''
Desafio 
Pergunte ao usuário quantos litros de água ele bebeu e defina 
um valor recomendado
'''

litros_agua = int(input('Quantos litros de aguá você bebeu? '))
if litros_agua >= 5:
    print('Parabéns você está hidratado')
else:
    print('Precisa beber mais água')
