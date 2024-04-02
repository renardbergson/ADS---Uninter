# possuem uma estrutura que LEMBRA um array em JavaScript, porém, aqui usa-se parênteses e a estrutura é imutável, não é possível inserir ou excluir itens através de linhas de código.

'''
  Cria uma função que receba argumentos indefinidamente (tupla) e que depois exiba na tela a soma de todos eles.
'''

def soma (*num):
  soma = 0
  print('Tupla: {}' .format(num)) # neste caso, a tupla ~e criada automaticamente
  for i in num:
    soma += i
  return soma

print('Resultado da soma:', soma(2, 4, 6, 8))