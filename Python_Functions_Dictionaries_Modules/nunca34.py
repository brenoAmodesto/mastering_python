"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

"""





def soma(*args):
    total = 0
    for numero in args:
        total += numero
        print(total, numero)
    return total


soma_var = soma(1,2,3,4,5,6)
print(soma_var)