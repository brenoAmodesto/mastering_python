"Qual letra apareceu mais vezes na frase"




alfa = "abcdefghijklmnopqrstuvwxyz"

frase = "Augusto modesto"



loop = -1
x = 0
x2 = ""

while loop < len(frase) :
    loop += 1
    
    t = alfa[loop]
    
    t1 = frase.count(t)

    if x < t1:
        x = t1
        x2 = t
    


print(f"Letra {x2} apareceu {x} vezes ")


