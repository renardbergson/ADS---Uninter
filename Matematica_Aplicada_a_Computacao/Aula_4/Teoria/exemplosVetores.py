'''
  QUESTÃO 1

  Considere um vetor que armazena os preços de venda, em dólares, de algumas mercadorias anunciadas em um comércio eletrônico:

  vetor=(22, 12, 54, 89, 11)

  Supondo que a cotação do dólar corresponde a 5 reais, utilizando a biblioteca "numpy", obtenha um vetor final, que contenha os preços dessas mercadorias com os valores convertidos para real e exiba-o.
'''

import numpy as np;

vetor = np.array([[22, 12, 54, 89, 11]]);
vetor2 = 5 * vetor;

print("QUESTÃO 1");
print(vetor2);
print();

# observe que esse algorítmo funciona como uma eventual soma, feita utilizando um laço de repetição

'''
  QUESTÃO 2

  Considere um vetor "custo", que armazena, em dólar, o preço de custo de algumas mercadorias:

  custos = [18, 4, 39, 61, 8]

  Considere também o vetor "precos", que armazena o preço de venda, em dólares, dessas mercadorias:

  precos = [22, 12, 54, 89, 11]

  A margem de lucro corresponde ao preço de venda menos o preço de custo. Sendo assim, utilizando a biblioteca "numpy", obtenha um vetor final, que contenha essa margem, em dólar, para cada uma das mercadorias.
'''

precos = np.array([[22, 12, 54, 89, 11]]);  
custos = np.array([[18, 4, 39, 61, 8]]);
lucros = precos - custos;

print("QUESTÃO 2");
print(lucros);
print();

# neste caso, foi feita uma subtração entre os respectivos elementos de cada vetor

'''
  QUESTÃO 3

  Considere um vetor "v", que armazena, em dólar, o preço de venda de algumas mercadorias:

  v = [18, 4, 39, 61, 8]

  Considere também o vetor "f", que armazena, em dólar, o preço do frete de cada uma delas:

  f = [3, 2, 1, 4, 1] 

  Obtenha um vetor final, que contenha o valor de cada mercadoria mais o respectivo valor de frete
'''

print("QUESTÃO 3");
v = np.array([[18, 4, 39, 61, 8]]);
f = np.array([[3, 2, 1, 4, 1]]);
vf = v + f;
print(vf);
print();

"""  
  Em uma instituição de ensino, os alunos matriculados em uma determinada disciplina realizaram 4 atividades avaliativas. As notas obtidas por um dos estudantes estão armazenadas no vetor "notas", e o vetor "pesos" possui os valores referentes ao peso de cada avaliação, em representação decimal.

  notas = (90, 85, 70, 100);
  pesos = (0.2, 0.2, 0.3, 0.3);

  A média do estudante pode ser obtida pelo produto escalar dos vetores "notas" e "pesos". O termo "produto escalar" está associado à multiplicação de vetores, onde é feita a multiplicação entre seus respectivos componentes e depois a soma dos produtos dessas operações, resultando em um número, que é o seu produto escalar. 
  
  Através da biblioteca "numpy, determine a média do estudante.
"""
print("QUESTÃO 4");
notas = np.array([[90, 85, 70, 100]]);
pesos = np.array([[0.2, 0.2, 0.3, 0.3]]);
media = np.inner(notas, pesos);
# "inner" porque "produto escalar" também pode ser chamado de "produto interno"
# esse método multiplicará cada componente entre os dois vetores e somará o produto dessas operações
print(media);

