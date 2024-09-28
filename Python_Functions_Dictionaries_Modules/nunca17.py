lista = ['Breno', 'Augusto', 'Modesto', 'Lobão', 'Martins', 'Luana', 'Lucas']

t = range(0,len(lista),1)

for x, m in zip(lista, t):
    print(m, x)
    

for item in enumerate(lista):
    print(item)
