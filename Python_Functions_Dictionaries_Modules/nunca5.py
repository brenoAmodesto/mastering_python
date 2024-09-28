"""
Adição
Subtração
Divisão
Multiplicação

"""


while True:
    
    entrada = input(" Digite 1- Somar\n Digite 2- Subtrair \n Digite 3- Multiplicar\n Digite 4- Divisão\n")
    p1 = input("Digite o primeiro numero")
    p2 = input("Digite o segundo numero")

    p1 = int(p1)
    p2 = int(p2)
    entrada = int(entrada)

    if entrada == 1:
        somar = p1 + p2
        print(somar)
    elif entrada == 2:
        subtrair = p1 - p2
        print(subtrair)
    elif entrada == 3:
        multiplicar = p1 * p2
    elif entrada == 4: 
        dividir = p1 / p2
        print(dividir)
    


    sair = input("Digite sair para sair!").lower().startswith('s')

    if sair is True:
        break

    n = 3
    if n % 2 == 0 and n > 2 and n < 5:
        print("Not Weird")