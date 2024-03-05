'''
  Utilizando o laço FOR, escreva um algorítmo que calcule a média dos números pares de 1 a 100 (ambos inclusos).

  Lembre-se que, a média é a soma dos elementos dividida pela quantidade deles.
'''

soma = 0
qtd = 0

for num in range (1, 101):
  if(num % 2 == 0):
    soma += num #soma = soma + num
    qtd += 1 #qtd = qtd + 1

media = soma / qtd

print('A média dos números pares dentro do intervalo de 0 a 100 é igual a {}' .format(media))