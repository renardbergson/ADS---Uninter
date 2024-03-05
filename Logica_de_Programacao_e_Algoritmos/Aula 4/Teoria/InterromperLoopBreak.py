'''
  Usando laço de repetição e o comando "break", escreva um algorítmo que fique recebendo frases ou palavras digitadas pelo usuário. Encerre o algorítmo, quando a palavra digitada for "sair"
'''

print('Digite uma mensagem e eu irei repeti-la para você!')
print('Para encerrar digite "sair".')

while True: #não há uma condição, o loop permanecerá indefinidamente
  texto = input('')
  print('"', texto, '"')
  
  if (texto == 'Sair' or texto == 'sair'):
    print('O programa foi encerrado!')
    break