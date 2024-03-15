'''
  1 - Escreva uma função que calcule o fatorial de um número recebido e retorne o seu resultado.` 
  2 - Faça uma validação dos dados por meio de uma outra função, permitindo que só números positivos
  sejam aceitos
  3 - Por fim, crie o help dessa função

  Ps: o fatorial de zero é igual a 1
'''

def valida_int (pergunta):
  '''
    pergunta = texto personalizável a ser exibido na tela como solicitação

    Essa função verifica se o número digitado é maior ou igual a zero.
    Enquanto o número for menor que zero, o usuário terá que digitá-lo novamente.
    Se o número for igual ou maior que zero, seu fatorial será exibido na tela.
  '''
  x = int(input(pergunta))
  while x < 0:
    print('Não é permitido obter o valor de números negativos! \n')
    x = int(input(pergunta))
  fatorial(x)
    

def fatorial (num):
  fat = 1

  if num == 0:
    return print('{}! = {}' .format(num, fat))
  for i in range (num, 0, -1):
    fat = fat * i
  return print('{}! = {}' .format(num, fat))

  '''
    repare a indentação do segundo return, fora do loop, para retornar somente o último valor 
    assumido por "fat" no laço. Caso contrário, retornará o primeiro valor assumido, que é igual a 1
  '''

valor = valida_int('Digite um número para descobrir seu fatorial: ')