def imprime_com_condicao (num, funCond):
  if funCond (num): # se a as funções "par" ou "impar" retornarem True, mostre o número
    print(num)

def par (x):
  return x % 2 == 0

def impar (x):
  return not par(x) # o inverso de "par", só que par precisa receber X

#verificação
imprime_com_condicao(5, par)