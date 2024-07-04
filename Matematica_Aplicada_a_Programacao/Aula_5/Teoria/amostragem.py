'''
  Quando pensamos em Amostra, é importante que saibamos o tamanho dela, ou seja, qual é a quantidade de elementos necessária para que nós tenhamos um estudo mais exato possível. Para isso, podemos utilizar a fórmula de Slovin:

  n = N / 1 + Ne², em que "n" é o tamanho da amostra, o que vamos obter, "N" é o total de elementos e "e" é a margem de erro.

  QUESTÃO 1

  Considerando que será realizado um estudo relacionado a 20.000 pessoas e que apenas uma parte dessas pessoas fará parte de forma efetiva, qual é o tamanho da amostra considerando uma margem de erro de 2%?
'''
from math import ceil; # arredonda para o próximo inteiro
N = 20000;
e = 0.02;
n = ceil( N / (1 + N * e**2) );
print(f'O tamanho da amostra é de {n} pessoas');