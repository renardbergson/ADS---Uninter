'''
  QUESTÃO 1

  Considere uma indústria que produz teclados para um modelo de notebook. Sabendo que o custo unitário de produção corresponde a R$ 28,00 e que, mensalmente x unidades são produzidas, podemos expressar o custo mensal de produção "C" em uma função da quantidade de teclados produzidos. Do ponto de vista analítico, multiplicar 28 por X, que é a quantidade sendo produzida.

  A função que representa o problema em questão é: C(x) = 28x

  É possível representar graficamente a função anterior, usando as biblioteca "numpy" "matplotlib", em conjunto. Neste caso, como não foi especificado valores para x, com "numpy" atribuiremos, de forma automática, valores para x em uma linha reta (linear) e, com "matplotlib", construiremos o gráfico.
'''

import numpy as np;
import matplotlib.pyplot as plt;
print("QUESTÃO 1");
x = np.linspace(0, 10, 100); # nosso espaço linear é um conjunto que vai de 0 a 10, tendo 100 valores pra x dentro desse intervalo
y = 28*x;
plt.plot(x, y);
grafico = plt.show();
print(grafico);
print();

'''
  QUESTÃO 2

  Supondo que a produção em um determinado mês foi de 2344 unidades, calcule o respectivo custo.
'''

print("QUESTÃO 2");
_x = 2344;
_y = 28*_x;
print(_y);
print();

'''
  QUESTÃO 3

  A função quadrática que relaciona o lucro mensal de um estacionamento com o preço cobrado por hora é:

  L(x) = -340x² + 5700x - 9500

  Onde x é o preço cobrado por hora e L é o lucro mensal. Com base nessas informações:

  a - construa o gráfico da função
  b - obtenha o preço que maximiza o lucro (x vértice)
  c - obtenha o respectivo lucro máximo

  Para calcular x vértice: xv = -b
                                2a

                           yv = - delta    (sendo delta = b² - 4ac)
                                   4a
'''

print("QUESTÃO 3");
print("a - Gráfico da função")
X = np.linspace(0, 16, 100); # podemos fazer testes com outros valores
Y = -340*X**2 + 5700*X - 9500;
plt.plot(X, Y);
grafico2 = plt.show();
print(grafico2);
print();

# ===========================
print("b - X vértice");
a = -340;
b = 5700;
xv = -b / (2*a); # obter x vértice
print(f'{xv:.2f} é o valor que maximiza o lucro');
print();

# ===========================
print("c - Lucro máximo");
c = -9500;
delta = b**2 - 4*a*c;
yv = - delta / (4*a); # obter y vértice
print(f'{yv:.2f} é o lucro máximo');