'''
  Uma empresa produz carregadores para um determinado modelo de telefone celular e precisa obter a função que relaciona o lucro mensal com o preço de venda dos carregadores. Os custos fixos mensais da empresa correspondem a R$ 47.500,00. Para um preço de venda de R$ 12,00 por unidade, o lucro mensal corresponde a R$ 22.000,00. Quando cada carregador é vendido por R$ 20,00, o lucro mensal é de R$ 20.450,00. Obtenha o polinômio interpolador que relaciona o lucro y com o preço de venda x
'''

from scipy.interpolate import *;
x = [0, 12, 20];
y = [-47500, 22000, 20450];
''''
  Pense...

  I - Se a empresa não produzir nada (x = 0), mesmo assim, o custo mensal é de R$ 47.500,00. Como estamos falando de CUSTO, tratamos como um valor negativo.
  II - Se o preço for R$ 12,00 (x = 12), então o lucro é de R$ 22.000,00 (y = 22000)
  III - Se o preço for R$ 20,00 (x = 20), então o lucro é de R$ 20.450,00 (y = 20450)
'''
p = lagrange(x, y);
print(p); 
# no final, 4.75e+04 = 4.75 * 10⁴ (resultado apresenta uma notação científica normalizada)