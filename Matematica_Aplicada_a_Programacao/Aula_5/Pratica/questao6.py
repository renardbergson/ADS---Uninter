'''
  Uma série de TV teve 10 episódios com as seguintes durações, em minutos: 35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
  Obtenha o desvio padrão por meio do Python.
'''
import pandas as pd;
x = {'duracoes':[35, 34, 26, 32, 37, 28, 27, 33, 36, 32]};
d = pd.DataFrame(x);
desvioPadrao = d['duracoes'].std();
print(f'O desvio padrão referente a duração dos elementos em questão é de {desvioPadrao:.2f}');