# Lista do Téo
teo_data = [ "Teo", "Calvo", 27, "Nah", "Via Varejo", ['Ana', "Clara", "Marcela"]]
nah_data = ["Nah", "Ataide", 29, "Teo", "Studio.Artesanah"]
nah_data.append( ['Jair', 'Carlos'] )

nah_data

len( nah_data )
len( teo_data )


# Programa maluco do Ayrton
new_teo_data = [] # Criando uma lista vazia!
for i in range( len(teo_data) ):

    v = teo_data[i]
    
    if type(v) == str:
        if i < 2:
            new_teo_data.append(v.upper())
        else:
            new_teo_data.append(v.lower())
    
    elif type(v) == list:
        new_list = []
       
        for j in v:
            if i < 2:
                new_list.append( j.upper() )
            else:
                new_list.append( j.lower() )
       
        new_teo_data.append( new_list )
    
    else:
        new_teo_data.append(v)

teo_data.append( "Kira" )
teo_data

# Concatenação ou extensão de listas
teo_data.extend( [ 'Caes de aluguel', 'Last of Us', 'Sons fo Anarchy' ] )
[1,2,3] + [4,5,6]

teo_data[::2]

# criando um sequencia 
list( range(1,10) )

# List compression ( compressão de listas)
raquel_list = [10, 25, "Teo", 1.82, "Nah", 100]

raquel_nova = []
for i in raquel_list:
    if type(i) == int:
        raquel_nova.append(i)
    else:
        pass

raquel_nova = [ i for i in raquel_list if type(i) == int ]
numeros = [ i**2 for i in range(1,11) ]

pares = [ i for i in range(11) if i % 3 == 0 ]

## Tuplas
# Foma mais bizarra de se definir tuplas e: "tuplas são listas imutaveis"

minha_tupla = ( "Teo", "Calvo", 27, "Nah", "Via Varejo", ['Ana', "Clara", "Marcela"] )

minha_tupla[0] = "Teodoro" # Isso não funciona! Pois tuplas são imutaveis

nova_tupla = 1,2

# Exercicio
A = 10
B = 20

# Troque o valor de A por B e de B por A
C = A
A = B
B = C

B, A = A, B

tupla = 1,2,3,5,6,7,8,9
a, b, *_, d = tupla
