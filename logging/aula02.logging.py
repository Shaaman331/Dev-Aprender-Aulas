'''
Logging em Python

* Logging é a maneira de rastrear os eventos que acontecem quando executamos nosso programa. 
É uma das ferramentas importantes usadas por desenvolvedores de software para fins de execução e depuração. 
Existem muitas situações em que temos que fazer algumas alterações no código porque obtivemos um erro ou 
um resultado inesperado.  

* Registrar um amigo em tais situações. Usando isso, podemos encontrar a causa do problema em menos tempo e 
com menos trabalho. A palavra 'log' é usada aqui porque conhecemos as informações por meio de mensagens de log. 

* Você ficaria em dúvida por que não podemos usar a instrução print, o que seria mais simples do que importar um módulo 
e usar seus métodos? A razão é que com a impressão, sim, podemos encontrar o problema. 
Mas isso funciona bem com problemas simples. Quando temos que depurar o problema complexo, a abordagem de 
impressão falha.

Níveis de registro em Python

1. Degub : é usado quando se precisa de informações detalhadas, especialmente quando se trata de diagnóstico de problemas.

2. Info : é usado para confirmar que o programa está funcionando conforme o esperado

3. Warming : é usado para indicar que algo inesperado aconteceu ou pode acontecer no futuro

4. Error : É usado para saber sobre qualquer problema sério quando o software não consegue executar alguma função

5. Critial : indica um problema muito sério, quando o próprio programa pode não conseguir continuar a ser executado. 

Configuração básica

Como dito anteriormente, podemos armazenar as informações obtidas fazendo login em um arquivo, em vez de exibi-lo no console. Para isso, usamos a função basicconfig (** kwargs). Os argumentos comumente fornecidos para esta função são:

1. level - especifica que o nível de gravidade é definido pelo nível raiz.

2. filename - Especifica um arquivo no qual as informações devem ser armazenadas

3. filemode - especifica o modo em que o arquivo deve ser aberto. O modo padrão é 'a', o que indica que podemos anexar o conteúdo ao arquivo.

4. format- define o formato em que a mensagem de log é inserida no arquivo. 

Classes e funções no registro Python

Este módulo também possui classes e funções relacionadas para lidar com diferentes situações. 
Aqui estão os mais comuns:

1. Formatadores - definem a estrutura da saída. Podemos usar o conceito de formatação de string para definir o formato das mensagens de log.

2. Logger - Este é um objeto da classe Logger que pode ser usado para chamar as funções de log diretamente.

3. LogRecord - Esta função cria um arquivo de registro automático que consiste nas informações sobre todos os eventos sendo registrados, como o nome do registrador, a função, o número da linha, a mensagem, etc.

4. Handler - Os handlers são usados ​​para gerenciar as mensagens de log e são responsáveis ​​por despachar a mensagem correta para o destino requerido. O FileHandler, StreamHandler, HTTPHandler, SMTTPHandler são as subclasses de um Handler. 
'''

import logging #Importando o módulo
logging.basicConfig(    #Fornecendo o nivel usado
    filename='info.log', #Especifica o arquivo onde as imformações devem ser armazenadas
    level= logging.DEBUG, #Espeficica o nível de gravidade definido pela raiz
    format='%(levelname)s %(asctime)s : %(message)s', #Define o formato que a mensagem de log é inserida no arquivo
    datefmt='%d/%m?%Y %H:%M:%S'# Define o formato de data e hora
)

logger = logging.StreamHandler() #  # Cria instancia de gerenciamento
logging.getLogger('').addHandler(logger) #Cria instancia e usa para chamar o logger

logging.debug('Isso é uma mensagem nivel debug') #Usando o objeto para chamar a função Debug
logging.info('Issso é uma mensagem nivel info') #Usando o objeto para chamar a função Info
logging.warning('Isso é uma mensagem nivel warning') #Usando o objeto para chamar a funçãp Warning
logging.error('Isso é uma mensagem nivel error') #Usando o objeto para chamar a função Error
logging.critical('Isso é uma mensagem nivel critical') #Usando o objeto para chammara função Critical 
