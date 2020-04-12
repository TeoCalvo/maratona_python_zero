meu_nome = "Teodoro Calvo"

i = 0
while i < len(meu_nome):
    print( meu_nome[i] )
    i += 1

for letra in meu_nome:
    print(letra)

# Vamo contar quandos numero são divisiveis por 5 entre 2000 e 3500

contador = 0 # Inicia o contador dos divisiveis por 5
for i in range(2000,3501): # Nosso range percorrendo de 2000 a 3500
    if i % 5 == 0: # Verifica se o i éehdivisivel por 5
        print(i, "eh divisivel por 5")
        contador += 1
    else:
        pass # Não faz nada

print("Temos", contador, "numeros entre 2000 a 3500 que sao divisives por 5")


