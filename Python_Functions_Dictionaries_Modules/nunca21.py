"""
Imprecisão de ponto flutuante
Double-precision-floating-point-format-IEEE-37774

"""

import decimal


numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2

print(round(numero_3, 2))