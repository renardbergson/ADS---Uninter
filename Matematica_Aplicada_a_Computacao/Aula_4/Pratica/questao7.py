'''
  Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u-v utilizando o Python
'''
import numpy as np;
u = np.array([[3, 4, 8]]);
v = np.array([[10, 12, -1]]); # o último da 9, porque 8 - (-1) = 9
subtracao = u - v;
print(subtracao);