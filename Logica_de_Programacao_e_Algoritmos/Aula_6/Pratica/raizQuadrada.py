'''
    Neste exemplo, estamos importando a biblioteca externa "math" e usando-a para obter a raíz de um número
'''

# importando a biblioteca toda
import math

numero = int(input('Insira um número inteiro: '))

print('A raíz quadrada de {} é igual a: {}' .format(numero, math.sqrt(numero)))

# importando só a função desejada
from math import sqrt

print('A raíz quadrada de {} é igual a: {}' .format(numero, sqrt(numero)))
