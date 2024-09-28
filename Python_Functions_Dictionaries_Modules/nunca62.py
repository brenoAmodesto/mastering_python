# Entendendo os seus prórpios módulos Python
# O primeiro módulo executado chama-se __main__
# Vocẽ pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes
# Nos caminhos de sys.path

import sys
import nunca62_m

try:
    import sys
    sys.path.append('PATH')
except ModuleNotFoundError:
     ...

print('Este módulo se chama', __name__)

print(*sys.path, sep='\n')

print(nunca62_m.variavel_modulo)
