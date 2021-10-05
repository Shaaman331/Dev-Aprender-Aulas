'''
O format()método permite que você formate partes selecionadas de uma string.
* Às vezes, há partes de um texto que você não controla, talvez eles vêm de um banco de dados ou da 
entrada do usuário?

* Para controlar esses valores, adicione marcadores de posição (colchetes {}) no texto e execute os valores 
por meio do format()método: 


'''
#Formatando Strings
aluno = 'Lucca'
nome_do_curso = 'Fotografia'
mensagem_introdução = f'Bem vindo ao curso de {nome_do_curso} {aluno}'
print(mensagem_introdução)

prince = 50
txt = 'The prince is {} dollars'
print(txt.format(prince))
