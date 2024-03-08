'''
  Escreva um algorítmo em que o usuário insira 3 valores, representando os 
  lados de um triângulo. Verifique se os valores fornecidos formam um triângulo
  e classifique-o como:

  a - Equilátero (três lados iguais)
  b - Isósceles (dois lados iguais)
  c - Escaleno (três lados diferentes)

  Lembre-se que, para formar um triângulo, nenhum dos lados pode ser igual a zero
  e que um lado nao pode ser maior que a soma dos outros dois lados!
'''

a = int(input('Insira o tamanho do 1º lado (número inteiro): '))
b = int(input('Insira o tamanho do 2º lado (número inteiro): '))
c = int(input('Insira o tamanho do 3º lado (número inteiro): '))

if (a > 0) and (b > 0) and (c > 0):
  if(a + b > c) and (a + c > b) and (b + c > a): 
    if (a == b and a == c):
      print('Você criou um triângulo EQUILÁTERO (3 lados iguais)')
    else:
      if (a != b and a != c and b != c):
        print('Você criou um triângulo ESCALENO (3 lados diferentes)')
      else:
        print('Você criou um triângulo ISÓSCELES (2 lados iguais)')
  else:
    print('Não é possível criar um triângulo, sendo um lado maior que a soma dos demais!')
else:
  print('Não é possível criar um triângulo com um dos lados igual a zero!')