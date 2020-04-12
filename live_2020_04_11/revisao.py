## Strings

nome = "Téo"
sobrenome = "Calvo"

## Métodos de string
print( nome.lower() ) # Caixa Baixa 
print( nome.upper() ) # Caixa Alta

# Operacoes com string
nome_completo = nome + ' ' + sobrenome

# Slicing de String
nome_completo[0] # Primeiro caracter da string
nome_completo[-1] # Ultimo caracter da string
nome_completo[:3] # Pega os três primeiros caracteres

nome_completo[::2] # Salta de 2 em 2
nome_completo[::-1] # Ordem invertida da string

## Numeros
a = 1 # Isso eh inteiro
b = 1. # isso eh um float
c = a + b # Isso eh um float
d = a - b

e = a * b # Mutliplacao
f = a / b # Divisão com resto
g = a // b # Inteira parte da divisão
h = a ** b # leia-se 'a' elevado a 'b'

# Booleanos
verdade = True
mentira = False

# Operações lógicas
a == b # Operação igualdade
a != b # Diverença
a > b # Maior
a < b # Menor
0 < a < 100 # A está entre 0 e 100?

a > b and b > c # duas comparações com and (e)
a > b or b > c # Duas comarações com or (ou)

## Estrutura if, elif else
idade = 20

if idade > 70:
    print("Cuidado com sua saude")
elif idade >= 18:
    print("Beba a vondade")

## Laços de Repetição
count = 1
while count <= 10:
    print(count)
    count += 1