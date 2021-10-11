'''
Métodos Join e Split

* O join()método pega todos os itens em um iterável e os une em uma corda.
Uma string deve ser especificada como separador

*O split()método divide uma string em um Lista.
Você pode especificar o separador, o separador padrão é qualquer espaço em branco. 

'''
print('Método Join')
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) 
print()

print('Método Split')
txt = "welcome to the jungle"
x = txt.split()
print(x) 
print()

print('Divida a string,usando vírgula,seguida por um espaço,como separador:')
texto = "hello, my name is Peter, I am 26 years old"
x = texto.split(", ")
print(x) 
print()

print('Use um caractere hash como separador: ')
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x) 
print()

frase = 'Olá, bem-vindo ao treinamento Mestre da Automação'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
print()

nomes = 'Raquel, Lucca, Carol, Daniel, Marco'
print(nomes.split())
print(nomes.split(','))
print()

hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))
print()

#Como concatenar(combinar strings)
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print('#'.join(hashtags_separadas_por_espaco))
print()






