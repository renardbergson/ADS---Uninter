'''
  QUESTÃO 1
  
  Utilize o Python para gerar um conjunto de números inteiros que variam de -10 a
  20. Em seguida, verifique se o número -1 está neste conjunto
'''

import numpy as np;
conjunto = np.linspace(-10, 20, 31);
print(conjunto);
print(-1 in conjunto);