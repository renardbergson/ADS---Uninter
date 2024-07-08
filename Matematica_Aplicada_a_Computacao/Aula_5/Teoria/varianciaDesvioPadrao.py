'''
  Variância Populacional: população é o conjunto total de dados
  Variância Amostral: amostra é uma parte de um conjunto de dados

  Uma indústria alimentícia produz cookies americanos. No processo de fabricação, cada
  porção de massa é pesada antes de assar para que os cookies sejam produzidos com um mesmo padrão. Espera-se que cada porção tenha 50 gramas, mas, por diversos fatores há uma variação no peso das porções. 
  A seguir, temos uma "AMOSTRA" contendo os pesos, em gramas, de 20 porções de massa: 
  
  49,7; 50,9; 48,9; 49,8; 50,1; 50,2; 50,8; 49,2; 50,1; 50,0; 50,4; 48,8; 49,3; 49,5; 49,1; 50,6; 49,0; 49,7; 49,7; 50,2

  Analiticamente, como podemos obter a Variância e o Desvio Padrão? Neste caso, como se trata de uma amostra...
  
  Variância Amostral:
  I - Calculamos a média
  II - Subtraimos a média de cada elemento e elevamos o resultado ao quadrado 
  III - Somamos todos os valores obtidos no passo 2 
  IV - Dividimos o resultado da soma pelo total de elementos - 1 
  (*** se não estivermos falando de uma amostra, NÃO subtraimos o total de elementos por -1 ***)
  (*** mesmo em se tratando de uma população, se ela tiver 30 dados ou menos, geralmente também se utiliza a fórmula do Desvio Padrão Amostral, a qual considera o -1 ***)

  Desvio Padrão Amostral?
  I - Obtemos a Variância
  II - Obtemos a raiz quadrada da variância
  
  (O desvio padrão é um dado que gera uma faixa em torno da média, para mais e para menos. A maioria dos dados estará nessa região)

  Agora, por meio do Python, calcule o Desvio Padrão do conjunto de dados.
'''

import pandas as pd;
x = {'Pesos':[49.7, 50.9, 48.9, 49.8, 50.1, 50.2, 50.8, 49.2, 50.1, 50, 50.4, 48.8, 49.3, 49.5, 49.1, 50.6, 49, 49.7, 49.7, 50.2]};
p  = pd.DataFrame(x);
desvioPadrao = p['Pesos'].std();
print(f'Desvio Padrão: {desvioPadrao}');