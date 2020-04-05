print("Bem vindo a cervejaria do Python")

nome = input("Diga lá seu nome: ")

print("Muito obrigado pela visita, ", nome, ". Vamos começar seu cadastro.", sep="")

idade = input("Entre com sua idade: ")
idade = int(idade) # Conversao de texto para numero

if idade < 18:
    print("Pivete desgraçado, quase me engana. Vá para casa!")

elif 18 <= idade <= 59 :
    print("Opaaa! Estamos à disposição. Beba até cair!")

else:
    print("Ok! Mas cuidado com sua saúde.")

