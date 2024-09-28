# Exercicios
# Crie funções que duplicam, triplicam e quadriplicam
# o número recebido como paramêtro

def matematica(num1, num2, num3):

    def somar():
       
       return num1 + num3
        
    
    def multiplicar():
        
        return num1 * num3
    
    if num2 == '*':
        return multiplicar
    elif num2 == '+':
        return somar
    
    
    


v = matematica(2,'*',3)
s = matematica(2,'+',3)
print(v())
print(s())