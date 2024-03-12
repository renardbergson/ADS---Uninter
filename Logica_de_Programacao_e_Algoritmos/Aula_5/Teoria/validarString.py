'''
  Escreva uma função que receba uma string e realize uma validação, com base em um número mínimo e máximo de caracteres. Se estiver dentro dos limites estabelecidos, retorne VERDADEIRO, caso contrário, retorne FALSO.
'''

def verificaString (str):
  if len(str) >= 4 and len(str) <= 10:
    return 'Verdadeiro'
  
  return 'falso'

resultado = verificaString('amor e paixão')
print(resultado)