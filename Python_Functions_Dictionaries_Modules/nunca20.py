"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes da lista.
"""

import os

compras = []
lista = ''

while True:
    
    menu = input("Selecione uma das opções abaixo \n i -- inserir \n a -- apagar\n l -- listar")
    
    if menu == "l":
        if not compras:
            print("A lista está vazia")
        
        else:

            for d, c in enumerate(compras):
                print(d, c)

    elif menu == "a":
        
        x = input("Digite o indice que deseja apagar")
        
        try:
            indice = int(x)
            del compras[indice]        
        
        except ValueError:
            print("Por favor digite numero int")
        except IndexError:
            print("Valor não existe")

    
    elif menu == "i":
        os.system('clear')
        
        inserir = input("Digite o item")
        compras.append(inserir)
    

    
         
         


    
    

   
    