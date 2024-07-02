'''
  Considere as matrizes:

  A = {3 5 9          B = {12 -6 7
       4 2 -3               3  0 2
       1 5 -5}             -1 10 1}
  
  Obtenha C = A * B
'''
import numpy as np;
A = np.array([[3, 5, 9], [4, 2, -3], [1, 5, -5]]);
B = np.array([[12, -6, 7], [3, 0, 2], [-1, 10, 1]]);
C = np.matmul(A, B);
print(C);