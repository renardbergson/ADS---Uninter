'''
  MATRIZES

  Uma matriz é um conjunto retangular formado por linhas e colunas, que pode ser representado entre colchetes ou entre parênteses.

A =  (3 2 -1 
      5 0 20)
      
  No caso do python, em particular, podemos trabalhar com matrizes importando a biblioteca "numpy", onde teremos representações de arrays com 2 colchetes. O colchete maior está associado ao array/matriz em si, e o colchete menor está associado a cada linha dessa matriz. Cada colchete interno deve ser separado por vírgula.
''' 
import numpy as np;

matriz = np.array([[3, 2, -1], [5, 0, 20]]);
print(matriz);