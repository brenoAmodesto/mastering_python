"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(*args):
    
    return "++++".join(args)

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia', 'Breno', 'teste', 'sacanagem,', 'bruxaria')
print(v)