# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.html
# Representados graficamente pelo diagrama de Venn
# Sets em python são mutáveis, porém aceitam apenas tipos imutávies como valor interno

#Criando um set
#set(iterável) ou {1, 2, 3}

#s1 = set() # vazio
#s1 = {'Luiz', 1,2,3} # com dados
#print(type(s1))

# Sets são eficientes para remover valores duplicados de iteráveis
# - eles não tem índexes;
# - eles não garantem ordem;
# - eles são iteráveis (for, in, not in)

#s1 = {1,2,3,3,3,3,3,3,1}
#print(s1)

# Métodos úteis:
# add, update, clear, discard
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1,2,3,4))
#print(s1)
s1.discard('Olá mundo')
#print(s1)
# Operadores úteis:
# união | união (union) - une
# intersecção & (intersection) - itens presentes em ambos
# diferença - itens presentes apenas no set da esquerda
# diferença simétrica ^ - itens que não estão em ambos
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2


print(s3)