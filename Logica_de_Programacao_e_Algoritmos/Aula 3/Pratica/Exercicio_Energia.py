'''
  Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e também o tipo de instalação: 

  R para Residencial
  I para Industrial
  C para Comercial

  Calcule o preço de acordo com os dados a seguir:

  Residencial 
    Faixa (kWh) ----------- Preço
    Até 500         ||      0,40
    Acima de 500    ||      0,65
  Comercial
    Faixa (kWh) ----------- Preço
    Até 100         ||      0,55
    Acima de 1000   ||      0,60
  Industrial
    Faixa (kWh) ----------- Preço
    Até 5000        ||      0,55
    Acima de 5000   ||      0,60
'''

print('--- CÁLCULO DA CONTA DE ENERGIA --- \n')

instalacao = input('Digite a inicial correspondente ao tipo de instalação consumidora. \n (R) - Residencial, (C) - Comercial, (I) - Industrial: ')

kWh = float(input('Insira a quantidade de Kwh consumida: '))

if instalacao == 'R' or instalacao == 'r':
  if kWh <= 500: 
    preco = 0.40
  else:
    preco = 0.65
elif instalacao == 'C' or instalacao == 'c':
  if kWh <= 100:
    preco = 0.55
  else:
    preco = 0.60
elif instalacao == 'I' or instalacao == 'i':
  if kWh <= 5000:
    preco = 0.55
  else:
    preco = 0.60

print('Você consumiu {} kWh e o total a pagar é igual a R$ {}' .format(kWh, kWh * preco))