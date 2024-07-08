'''
  Construa o gráfico da função y = x³ - 2x² + 12x-1 no intervalo [-3, 4]
'''

import matplotlib.pyplot as plt;
import numpy as np;

x = np.linspace(-3, 4, 100); 
# a qtd de números no intervalo poderia ser 10, 1000...
# o importante é gerar um gráfico que esteja de acordo com o esperado
y = x**3 - 2*x**2 + 12*x-1;

plt.plot(x, y);
print(plt.show());