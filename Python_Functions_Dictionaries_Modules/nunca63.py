import importlib

import nunca63_m

print(nunca63_m.variavel)

for i in range(10):
    importlib.reload(nunca63_m)
    print(i)

print('Fim')