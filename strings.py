print("Olá, seja bem vindo!") # Exibe mensagem de boas vindas
nome = input("Digite seu nome: ") # Recebe dado do usuario
print( 'Olá ', nome, ", seja bem vindo!", sep="" ) # Exibe o nome do usuário

# Descobrindo o tipo da variável nome
type( nome ) # str é string

# Caixa alta de string
nome_maisculo = nome.upper()
print(nome_maisculo)

# Caixa baixa de string
nome_minusculo = nome.lower()
print(nome_minusculo)

# replace substring
nome.replace( "Teo", "Lara" ) #substitui todas ocorrencias

###### POSICOES DA STRING
qtde_caracteres = len(nome) # quantidade de caracteres

# Ultima letra do meu nome
nome = "Teodoro Calvo"
nome[-1]

# Fatiamento - Slice
nome[0] # Primeira posicao

nome[0:3] # nome[start:stop]
nome[:3] # mesma coisa que o de cima

nome[:: ] # nome[start:stop:step] sintaxe completa de fatiamento
nome[::2]

nome.find( ' ' )

nome[7]
nome[:3] + nome[ 7+1 : 7+1+3 ]

nome[:3] + nome[ nome.find(" ")+1 : nome.find(" ")+1+3 ]




