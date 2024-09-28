#dir, hasattr e getattr em Python
string = 'luiz'
metodo = 'upper'

print(string)


if hasattr(string, 'upper'):
    print('Existe upper aqui')
    print(string.upper())