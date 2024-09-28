# try, excpet, else e finally

try:
    print('ABRIR ARQUIVO')
    8/0

except ZeroDivisionError:
    print('DIVIDIU ZERO')

finally: 
    print('FECHAR ARQUIVO')