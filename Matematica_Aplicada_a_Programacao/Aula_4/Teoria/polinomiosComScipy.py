'''
  Para obter um polinômio interpolador, utilizamos o seguinte raciocínio:

  from scipy.interpolate import *;

  x = []
  y = []
  p = lagrange(x, y);
  print(p);

  O que é interpolação? Significa achar uma função que passa por um conjunto de pontos conhecidos.
'''

''''
  QUESTÃO 1 

  Por meio do python, obtenha o polinômio que interpola os pontos A(4, 2), B(7, -1), C(10, 12), e D(11, 15)
'''

print("QUESTÃO 1")
from scipy.interpolate import *;
x = [4, 7, 10, 11]; # x é sempre a primeira coordenada dos pontos
y = [2, -1, 12, 15]; # y é sempre a segunda coordenada dos pontos
p = lagrange(x, y);
print(p);
print();

'''
  QUESTÃO 2

  Considerando a concentração média de partículas por milhão (ppm) de um certo poluente, em uma determinada região está se alterando com o passar do tempo, e que os dados obtidos durante 4 anos foram:

  Ano             1     2     3     4
  Concentração    80    95    110   122 

  Obtenha o polinômio que interpola esses dados
'''

print("QUESTÃO 2")
X = [1, 2, 3, 4];
Y = [80, 95, 110, 122];
P = lagrange(X, Y);
print(P);