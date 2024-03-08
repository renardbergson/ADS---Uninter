'''
  Escreva um algorítmo que calcule a tabuada de todos os números de 1 a 10 e que, para cada número sejam feitas também multiplicações nos intervalos de 1 a 10.

  Resolva o exercício das 3 formas a seguir:

  1 - Usando dois laços WHILE
  2 - Usando dois laços FOR
  3 - Usando WHILE + FOR
'''

print('--- Calculadora com dois laços WHILE --- \n')

num = 1

while (num < 11):
  mult = 1

  while(mult < 11):
    print('{} x {} = {}' .format(num, mult, num * mult))
    mult += 1

  print('')
  num += 1

# ======================================================
print('--- Calculadora com dois laços FOR --- \n')

for num in range (1, 11, 1):
  for mult in range (1, 11, 1):
    print('{} x {} = {}' .format(num, mult, num * mult))

  print('')

# ======================================================
print('--- Calculadora com laço WHILE + FOR --- \n')

for num in range (1, 11, 1):
  mult = 1

  while (mult < 11):
    print('{} x {} = {}' .format(num, mult, num * mult))
    mult += 1

  print('')

# Perceba a necessidade de incrementar as variáveis manualmente apenas no laço WHILE...