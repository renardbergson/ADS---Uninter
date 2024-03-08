'''
  Utilizando os laços de repetição FOR e WHILE, resolve os algorítmos a seguir:

  1 - Print os números inteiros de 3 até 12, com 12 incluso

  2 - Print os inteiros de 0 até 9, excluindo o 9, com passo de 2
'''

print('Números inteiros de 3 a 12 com laço FOR \n')

for num in range (3, 13):
  print(num)
print('')
# ===================================================

print('Números inteiros de 3 a 12 com laço WHILE \n')

num = 3
while (num < 13):
  print(num)
  num += 1
print('')
# ===================================================

print('Números inteiros de 0 a 9 (menos o 9), com passo 2 e laço FOR \n')

for num in range (0, 9, 2):
  print(num)
print('')
# ===================================================
  
print('Números inteiros de 0 a 9 (menos o 9), com passo 2 e laço WHILE \n')

num = 0
while (num < 9):
  print(num)
  num += 2