'''
  Utilizando a fórmula de Slovin e o Python, calcule o tamanho da amostra referente a uma população de 200.000 dados considerando uma margem de erro de 4%?

  N / 1 + Ne²
'''
from math import ceil; 
N = 200000;
e = 0.04;
n = ceil( N / (1 + N * e**2) ); # arredondar para o inteiro mais próximo
print(f'O tamanho da amostra é de {n}');