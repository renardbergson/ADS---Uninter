'''
  Usando laço de repetição, crie um algorítmo que receba um valor do tipo INTEIRO via teclado

  O programa só deve aceitar valores INTEIROS e POSITIVOS

  Qualquer valor negativo ou igual a zero deve ser rejeitado e um novo valor solicitado
'''

numero = int(input('Digite um valor inteiro e maior que zero: '))

while (numero <= 0):
  numero = int(input('Digite um valor inteiro e maior que zero: '))

print('Ok, você digitou {}, encerrando o programa.' .format(numero))