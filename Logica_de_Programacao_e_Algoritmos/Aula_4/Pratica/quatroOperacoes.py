'''
  Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual das 4 operações matemáticas ele deseja realizar, incluindo também a opção "sair". Faça esse processo ser repetido, até que essa opção seja selecionada.
'''

print('Bem-vindo à calculadora Python!')
print('Suas opções são: \n \n (+) Adição \n (-) Subtração \n (*) Multiplicação \n (/) Divisão \n')

while True:
  op = input('Digite o símbolo da operação que deseja realizar ou "sair" para cancelar: ')

  if (op == 'sair' or op == 'Sair'):
    break

  if (op == '-' or op == '+' or op == '*' or op == '/'):
    num1 = float(input('Digite um número: '))  
    num2 = float(input('Digite um segundo número: '))  

    if (op == '-'):
      res = num1 - num2
      print('O resultado da operação {} {} {} é igual a {}' .format(num1, op, num2, res))
    elif (op == '+'):
      res = num1 + num2
      print('O resultado da operação {} {} {} é igual a {}' .format(num1, op, num2, res))
    elif (op == '*'):
      res = num1 * num2
      print('O resultado da operação {} {} {} é igual a {}' .format(num1, op, num2, res))
    else:
      res = num1 / num2
      print('O resultado da operação {} {} {} é igual a {}' .format(num1, op, num2, res))
  else:
    print('Operação Inválida!')
    break

  continue
print('Programa encerrado.')