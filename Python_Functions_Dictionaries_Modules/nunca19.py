"""
Exercício
Exiba os índices da lista

0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for i, x in enumerate(lista):
    print(i, x)