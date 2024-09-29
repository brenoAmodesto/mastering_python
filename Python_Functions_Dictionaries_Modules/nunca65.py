# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# copy, sorted, produtos.sort

import copy
from dados import produtos

# Exemplo usando list compreheension

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]


# print(*produtos, sep ='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)


# print(*produtos, sep ='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

print(*produtos, sep ='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')




# Do jeito que eu fiz

# deep_copy_produtos = copy.deepcopy(produtos)

# fator = 1.10

# for dicionarios in deep_copy_produtos:
#        preco = (dicionarios['preco'])
#        dicionarios['preco'] = round(dicionarios["preco"] * fator, 2)

# produtos_ordenados_nome = sorted(deep_copy_produtos, key=lambda x: x["nome"],  reverse=True)

# print(produtos_ordenados_nome)

# deep_copy_preco = copy.deepcopy(produtos_ordenados_nome)

# produtos_ordenados_preco = sorted(deep_copy_preco, key=lambda x: x["preco"])

# print(produtos_ordenados_preco)


