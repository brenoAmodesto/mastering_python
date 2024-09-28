"""
Split e join com list e str
Split - divide uma string
Join - une uma string

"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()



lista_palavras_x = []

for i, frase in enumerate(lista_palavras):
    lista_palavras_x.append(lista_palavras[i])

frases_unidas = ' '.join(lista_palavras_x)
print(frases_unidas)

