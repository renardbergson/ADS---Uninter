'''
  QUESTÃO 1

  Uma indústria de cadeiras gamer possui 3 modelos denominados A, B e C, e possui 2 fábricas chamadas de F1 e F2. Na fábrica F1 são produzidas as peças, na fábrica F2 é feita a montagem das cadeiras.

  Os custos de produção e de transporte associadas à fábrica F1 correspondem a:

      Custo de Produção                     Custo de Transporte
  A   R$ 400,00                              R$ 10,00
  B   R$ 480,00                              R$ 12,00
  C   R$ 600,00                              R$ 15,00

  Os custos de montagem e de transporte associadas à fábrica F2 correspondem a:

      Custo de Montagem                      Custo de Transporte
  A   R$ 31,00                               R$ 11,00
  B   R$ 37,00                               R$ 11,00
  C   R$ 48,00                               R$ 11,00

  Com base nessas informações e utilizando a biblioteca "numpy", determine os custos totais de produção e transporte referentes a cada modelo de cadeira gamer

  F1 = (400 10
        480 12
        600 15)

  F2 = (31 11
        37 11
        48 11)
'''

import numpy as np;
print("QUESTÃO 1")
F1 = np.array([[400, 10], [480, 12], [600, 15]]);
F2 = np.array([[31, 11], [37, 11], [48, 11]]);
custoTotal = F1 + F2;
print(custoTotal);
print();

'''
  Resultado da questão 1

      Custo total de Produção                Custo total de Transporte
  A   R$ 431,00                               R$ 21,00
  B   R$ 517,00                               R$ 23,00
  C   R$ 648,00                               R$ 26,00
'''

'''
  QUESTÃO 2

  Considerando os mesmos dados dos custos de produção e montagem das cadeiras gamer, referentes às fábridas F1 e F2, refaça o mesmo cálculo, adicionando um aumento de 10% sobre o custo total de fabricação e transporte
'''

print("QUESTÃO 2");
# Fator de aumento: 100% (valor inicial) + 10% = 110% = 1,1
# CUIDADO! Calcular aumento de porcentagem aqui não se faz com soma, mas com multiplicação
novoCustoTotal = custoTotal * 1.1;
print(novoCustoTotal);
print();

'''
  Resultado da questão 2

      Novo Custo de Produção (F1 e F2)        Novo Custo de Transporte (F1 e F2)
  A   R$ 474,1                                R$ 21,1
  B   R$ 568,7                                R$ 25,3
  C   R$ 712,8                                R$ 28,6
'''

'''
  QUESTÃO 3

  Multiplique as matrizes a seguir:

  A = {3 1 3    B = {100 50
       6 5 5}        50 100
                     50 50}

  Para prosseguir, multiplicamos cada elemento da primeira linha de A por cada elemento da primeira coluna de B e somamos os resultados: 3 x 100 + 1 x 50 + 3 x 50. A soma desses produtos resultará no primeiro número da nova matriz. Depois, fazemos o mesmo procedimento com os elementos da segunda linha de A com a segunda coluna de B, obtendo assim o segundo número da nova matriz. O procedimento continua, até que não reste mais linhas ou colunas. 

  Para realizar esse procedimento no python, podemos utilizar a biblioteca Numpy, através do método "matmul", passando as matrizes em questão como argumentos.
'''

print("QUESTÃO 3");
A = np.array([[3, 1, 3], [6, 5, 5]])
B = np.array([[100, 50], [50, 100], [50, 50]])
produtoDeAeB = np.matmul(A, B); 
print(produtoDeAeB);