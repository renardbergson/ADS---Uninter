'''
  Uma série de TV teve 10 episódios com as seguintes durações, em minutos: 35, 34, 26, 32, 37, 28, 27, 33, 36, 32. Por meio do Python, obtenha a média, a moda e a mediana dos dados
'''
import pandas as pd;
x = {'duracoes':[35, 34, 26, 32, 37, 28, 27, 33, 36, 32]};
d = pd.DataFrame(x);
media = d['duracoes'].mean();
moda = d['duracoes'].mode();
mediana = d['duracoes'].median();
print(f'Média: {media}')
print(f'Moda: {moda}')
print(f'Mediana: {mediana}')