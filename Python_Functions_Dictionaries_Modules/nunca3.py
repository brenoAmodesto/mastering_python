"""Faça um programa que peça ao usuário para digitar um número inteiro, 
informe se este número é par ou ḿipar. Caso o usuário não digite um número inteiro, 
informe que não é um número inteiro



numero_int = input("Digite um número inteiro")
numero_int = int(numero_int)
resto = numero_int % 2

if numero_int <= 0:  print("Não é um número inteiro") 

elif resto == 0
    print(f"O numero {numero_int} é par")
else:
    print(f"O numero {numero_int} é impar")

"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
hora = input("Digite a hora")

hora = hora.replace(":",'')

hora = int(hora)

hora = str(hora)

len = len(hora)


if len == 4:
    hora1 = hora[0:2]
    hora1 = int(hora1)

    if hora1 > 11 and hora1 < 17: print("Boa tarde")

    if hora1 > 18 and hora1 < 23: print("Boa noite")


if len == 3:
    hora2 = hora[0:1]
    hora2 = int(hora2)


if len == 2:
    print("Bom dia")
"""



"""Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". """



"""

nome = input("Digite seu nome")

len = len(nome)

if len == 4 or len < 4:
    print("Seu nome é curto")

if len == 5 or len == 6:
    print("Seu nome é normal")

if len > 6:
    print("Seu nome é muito grande")

"""
