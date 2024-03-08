'''
  Usando laço de repetição, Escreva um algorítmo que imprima na tela somente os valores 
  pares, dentro de um  intervalo especificado pelo usuário
'''

x = int(input('Insira um número inteiro para iniciar a contagem: '))
y = int(input('Insira um número inteiro para finalizar a contagem: '))


while (x <= y):
  if (x % 2 == 0):
    print(x)
  x = x + 1