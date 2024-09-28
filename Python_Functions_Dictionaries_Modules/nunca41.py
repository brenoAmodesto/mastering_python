# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# poppitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

p1 = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
}


tupla = ('nome', 'novo valor'),
p1.update(tupla)
print(p1)



#nome = p1.pop('sobrenome')
#print(p1.get('nome'))
#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))
#for chave in pessoa.keys():
#   print(chave)
# pessoa.setdefault('idade', 0)
# print(pessoa['idade'])


#for chave, valor in pessoa.items():
#    print(chave, valor)

# d1  = {
#     'c1': 1,
#     'c2': 2,
#     'l1': [0,1,2],
# }

# d2 = copy.deepcopy(d1)

# d2['c1'] = 1000
# d2['l1'][1] = 9999999 


# print(d1)
# print(d2)

