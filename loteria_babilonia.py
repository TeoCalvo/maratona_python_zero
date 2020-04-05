num_correto = 7
tentativas = 1

while tentativas <= 3:
    num_aposta = int( input("Entre com seu número da sorte: ") )
    if num_aposta == num_correto:
        print("Acertou, miserávi!")
        break
    elif num_aposta < num_correto:
        print("Tente um numero maior.")
    else:
        print("Tente um número menor.")
    tentativas += 1