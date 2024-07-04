'''
  Média: é o valor obtido pela soma de determinados elementos, dividido pela quantidade deles.
  
  Moda: dado que aparece o maior número de vezes em um determinado conjunto.
  
  Mediana: elemento que ocupa a posição central de um ROL, ou seja, o elemento que está no centro de um conjunto de dados ordenados. *** É IMPORTANTE QUE OS DADOS ESTEJAM ORDENADOS! *** Em conjuntos de contagem par, dividimos a quantidade de elementos por 2, para encontrar a posição do primeiro elemento que nos interessa, assim como o próximo elemento após ele. Por fim, somamos esses dois valores e dividimos por 2, obtendo assim a Média que, neste caso, será também a Mediana.

  Uma indústria alimentícia produz cookies americanos. No processo de fabricação, cada
  porção de massa é pesada antes de assar para que os cookies sejam produzidos com um mesmo padrão. Espera-se que cada porção tenha 50 gramas, mas, por diversos fatores há uma variação no peso das porções. 
  A seguir, temos uma amostra contendo os pesos, em gramas, de 20 porções de massa: 
  
  49,7; 50,9; 48,9; 49,8; 50,1; 50,2; 50,8; 49,2; 50,1; 50,0; 50,4; 48,8; 49,3; 49,5; 49,1; 50,6; 49,0; 49,7; 49,7; 50,2
  
  A partir destes dados, por meio do Python, obtenha a Média, a Moda e a Mediana
'''

import pandas as pd;
x = {'Pesos':[49.7, 50.9, 48.9, 49.8, 50.1, 50.2, 50.8, 49.2, 50.1, 50, 50.4, 48.8, 49.3, 49.5, 49.1, 50.6, 49, 49.7, 49.7, 50.2]};
# a biblioteca pandas trabalha considerando os dados como planilhas (linhas e colunas), sendo assim, o nome definido antes dos [] é como o nome de uma coluna
p  = pd.DataFrame(x);
media = p['Pesos'].mean();
moda = p['Pesos'].mode(); # a moda aparece na forma de um array, já que pode haver repetição de elementos
mediana = p['Pesos'].median();
print(f'Média: {media}');
print(f'Moda: {moda}');
print(f'Mediana: {mediana}');