# Variáveis livres + nonlocal
def fora():
    a = x

    def dentro():
        return a
    return dentro

dentro = fora(10)