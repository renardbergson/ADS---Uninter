'''
  Um cinema cobra preços diferentes para os ingressos, de acordo com a idade de uma pessoa. Se a pessoa tiver menos de 3 anos, o ingresso é gratuito, se tiver entre 3 e 12 anos, custa R$ 15, se tiver mais de 12, custa R$ 30. 

  1 - Escreva um laço em que seja perguntado a idade dos usuários, então, informa o preço dos ingressos

  2 - Encerre o laço, se o usuário digitar "sair"

  3 - Após encerrar o laço, mostre na tela: 
    a - o total de pessoas que compraram ingressos 
    b - o total arrecadado 
    c - a média de idade das pessoas
'''

print('--- Bem-vindo! ---')

totalVendas = 0
dinheiro = 0
somaIdades = 0

while True:
  idade = input('Digite a sua idade. Ex: "14": ')

  if (idade == 'sair'):
    break
  idade = int(idade)
  totalVendas += 1
  somaIdades += idade
  
  if (idade < 3):
    ingresso = 0
    print('Para você o ingresso é gratuito! \n')
  else:
    if (idade >= 3 and idade <= 12):
      ingresso = 15
      print('Seu ingresso custa R$ 15,00 reais. \n')
    else:
      ingresso = 30
      print('Seu ingresso custa R$ 30,00 reais. \n')
  dinheiro += ingresso
mediaIdade = somaIdades / totalVendas

print('Um total de {} pessoas compraram ingressos hoje.' .format(totalVendas))
print('O montante arrecadado foi igual a R$ {} reais.' .format(dinheiro))
print('A média de idade dos expectadores foi de {} anos.' .format(int(mediaIdade)))