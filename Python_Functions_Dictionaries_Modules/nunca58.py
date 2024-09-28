# Try, except, else e finally


try:
    a = 18
    b = 0
    print(b[0])
    c = a / b

except ZeroDivisionError:
    print('Dividiu por zero')
except NameError:
    print("B não está definido")
except Exception:
    print('ERRO DESCONHECIDO')

print('CONTINUAR')