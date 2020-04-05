num_ini = int( input("Entre com um numero para descobrir se é primo: ") )
teste = 0
num = 2
while num < num_ini:
    if num_ini % num == 0:
        print(num_ini, "não é primo")
        teste += 1
        break
    num += 1

if num_ini == 1:
    print(num_ini, "não é primo")  
elif teste == 0:
    print(num_ini, "é primo")
