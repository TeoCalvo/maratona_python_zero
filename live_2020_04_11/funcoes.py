def ola():
    print("Olá Mundo")

def fx( x ):
    return x ** 2

def soma(a=0, b=0):
    resultado = a + b
    return resultado

def eh_par( x ):
    ''' Função para identificar se o numero eh par ou impar.
    
    É esperado um valor numérico (inteiro) a ser passado.
    
    O retorno dessa função e um booleano
    '''
    if x % 2 == 0:
        return True
    else:
        return False

flag_pares = [ i for i in range(1,11) if eh_par(i) ]

dict_pares = { i: eh_par(i) for i in range(11) }
