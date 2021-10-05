'''Separando Strings'''

frase = "Olá, bem-vindo ao Treinamento Mestre da automação"
print(frase.split())
print(frase.split(","))
print(frase.split("-"))
nomes = "Tarcisio, Lucca, Carol, Raquel, Daniel"
print(nomes.split())
print(nomes.split(","))
hashtags = "music #guitar #gamaer #coder #python"
print(hashtags.split())
print(hashtags.split("#"))
print(hashtags.split("#",3))
'''Como concatenar(combinar) string'''
hashtag_separadas_por_espaços = hashtags.split(" ")
print(hashtag_separadas_por_espaços)
print(",".join(hashtag_separadas_por_espaços))
print(".".join(hashtag_separadas_por_espaços))
print(" ".join(hashtag_separadas_por_espaços))
