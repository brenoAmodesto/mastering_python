# List comprehension em Python
# List comprehension é uam forma rápida para criar listas
# a partir de iteráveis.

#print(list(range(10)))
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)


lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)


lista = [numero * 2
         for numero in range(10)]
#print(lista)

#Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p1', 'preco': 10, },
    {'nome': 'p1', 'preco': 30, },
]

produto_teste = {'nome': 'p1', 'preco': 20}


for produto in produtos:
   if produto['preco'] > 20:
       print({**produto, 'preco': produto['preco'] * 1.05})

#print({**produto_teste, 'preco': produto_teste['preco']})

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]


#print(*novos_produtos, sep='\n')

#p(novos_produtos)

#lista = [n for n in range(10)]
#print(lista)

# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p1', 'preco': 10, },
#     {'nome': 'p1', 'preco': 30, },
# ]

# novos_produtos = [
#     {**produto, 'preco':  produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if (produto['preco'] > 20 and produto['preco'] * 1.05 > 10)
# ]

# p(novos_produtos)



#nums = [54, 22, 15, 48, 332, 1265, 1, 664, 223, 156]
#evens = [num for num in nums if num%2==0]
#print(evens)



#def check_sum(x, y, z, n):

#x = 1
#y = 1
#z = 2
#n = 3


#new_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
#print(new_list)


#n = 20
