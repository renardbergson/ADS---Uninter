'''
  Usando laço de repetição e os comandos "continue" e "break" escreva um algorítmo que realize um login simples, em que o usuário deve informar usuário e senha.
'''

while True:
  login = input('Digite o seu username: ')

  if (login != 'renard'):
    print('Usuário inválido!')
    continue
  else:
    break

while True:
  senha = input('Digite a sua senha: ')
  
  if (senha != 'uninter'):
    print('Senha inválida!')
    continue
  else:
    break

print('Acesso concedido!')