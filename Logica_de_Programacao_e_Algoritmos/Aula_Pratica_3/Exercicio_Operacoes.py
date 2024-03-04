'''
  Escreva um algorítmo que leia 2 valores numéricos e que pergunte ao usuário qual operação ele deseja
  realizar: adição, subtração, multiplicação ou divisão. Depois, exiba na tela o resultado da operação
  desejada.
'''
print('--- CALCULADORA DE DOIS VALORES --- \n')

print('Para cancelar, digite qualquer caracter!')
op = input('Para prosseguir, digite o símbolo da operação que deseja realizar. \n (+) Adição, (-) Subtração, (*) Multiplicação ou (/) Divisão: ')

if (op != '+' and op != '-' and op != '*' and op != '/'):
  print('Você não digitou um símbolo válido, a operação foi cancelada.')
else:
  v1 = float(input('Insira um valor numérico qualquer: '))
  v2 = float(input('Insira novamente um valor numérico qualquer: '))

  if (op == '+'):
    soma = v1 + v2
    print('O resultado de {} {} {} é igual a: {}' .format(v1, op, v2, soma))
  if (op == '-'):
    sub = v1 - v2
    print('O resultado de {} {} {} é igual a: {}' .format(v1, op, v2, sub))
  if (op == '*'):
    mult = v1 * v2
    print('O resultado de {} {} {} é igual a: {}' .format(v1, op, v2, mult))
  if (op == '/'):
    div = v1 / v2
    print('O resultado de {} {} {} é igual a: {}' .format(v1, op, v2, div))