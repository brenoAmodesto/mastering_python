"""
Iterando strings com while
"""

nome = 'LuizOtávio' # Iteráveis

contador = -1

len = len(nome) - 1

nome3 = ''


while contador < len:

    contador = contador + 1
    
    #nova_string = nome[contador] + string

    nome1 = nome[contador]
    nome3 = nome3 + "*" + nome1


print(nome3)