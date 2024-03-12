'''
  Escreva uma função que receba uma string como parâmetro, e cria uma borda ao redor dela. A borda deve ser adaptável ao tamanho da string.
'''

def borda (str):
  tamanho = len(str)
  borda = '+' + ' ' + '-' * tamanho + ' ' + '+'

  if tamanho:
    print(borda)
    print('|', str, '|')
    print(borda)

borda('Lógica de Programação e Algoritmos')