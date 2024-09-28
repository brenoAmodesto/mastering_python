"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

"""


palavra_secreta2 = "breno"
string = ""

len = palavra_secreta2


tentativa = 0

for i in len:
        
        
    entrada = input(f"Palavra secreta digite a letra")
        
    if entrada in palavra_secreta2:
        string += entrada              
    
    else:
        string = string + "*"

print(string)
        
    
        

# for i in len:
    
#     entrada = input(f"Palavra secreta digite a letra")
#     x = palavra_secreta2.count(entrada)

#     if x > 0:
#         print(entrada)
    
#     else:
#         tentativa = tentativa + 1

# print(f"a quantidade de tentativas foi {tentativa}")