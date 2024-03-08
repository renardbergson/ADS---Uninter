'''
  Escreva um algorítmo que leia um valor digitado pelo usuário e que calcule quanta cédulas são necessárias para pagar esse valor. As seguintes regras devem ser adotadas:

  1 - Apenas números inteiros
  2 - Cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1

  Utilize um laço de repetição para evitar eventuais testes desnecessários
'''

valor = int(input('Digite um valor inteiro em R$ o qual você deseja sacar: '))

while True:
  if valor >= 100: #1
    cedulas_necessarias = valor // 100
    desconto = cedulas_necessarias * 100
    valor -= desconto
    print('Será necessário {} cédula(s) de CEM reais.' .format(cedulas_necessarias))
    if not valor:
      break
  if valor >= 50: 
    cedulas_necessarias = valor // 50
    desconto = cedulas_necessarias * 50
    valor -= desconto
    print('Será necessário {} cédula(s) de CINQUENTA reais.' .format(cedulas_necessarias))
    if not valor:
      break
  if valor >= 20: 
    cedulas_necessarias = valor // 20
    desconto = cedulas_necessarias * 20
    valor -= desconto
    print('Será necessário {} cédula(s) de VINTE reais.' .format(cedulas_necessarias))
    if not valor:
      break
  if valor >= 10: 
    cedulas_necessarias = valor // 10
    desconto = cedulas_necessarias * 10
    valor -= desconto
    print('Será necessário {} cédula(s) de DEZ reais.' .format(cedulas_necessarias))
    if not valor:
      break
  if valor >= 5: 
    cedulas_necessarias = valor // 5
    desconto = cedulas_necessarias * 5
    valor -= desconto
    print('Será necessário {} cédula(s) de CINCO reais.' .format(cedulas_necessarias))
    if not valor:
      break
  if valor:
    cedulas_necessarias = valor
    print('Será necessário {} cédula(s) de UM real.' .format(cedulas_necessarias))
    break