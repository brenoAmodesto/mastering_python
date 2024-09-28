"""
Exercicios com funções

Crie uma função que multiplica todos os argumentos
Não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

Crie uma função fala se um numero é par ou ímpar
Retorne se o número é par ou ímpar

"""


def multiplicar(*args):
    m = 1
    for n in args:
        m = m * n
        print(m)

    return m

var_m = multiplicar(10,2,3,4,5)
print(var_m)


def impa_pa(x):

    x = x % 2
   
    a = "par" if x == 0 else "impar"
    return a

    

var = impa_pa(2)
print(var)