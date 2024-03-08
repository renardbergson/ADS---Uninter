'''
  Usando laço de repetição, escreva um algorítmo para calcular a média aritmética, com base em 5 notas fornecidas pelo usuário
'''

nota = 1
soma = 0

while (nota <= 5):
  valor = float(input('Digite a sua {}ª nota: ' .format(nota)))
  nota += 1   #nota = nota + 1
  soma += valor   #soma + valor

media = soma / nota   #5
print('A sua média final foi: {}' .format(media))