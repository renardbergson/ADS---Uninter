'''
  QUESTÃO 4

  Para a entrada em uma residência, foram criadas 5 senhas numéricas: 452012,
  323233, 787910, 528917 e 683524. Por meio do Python, crie um programa que
  armazena estas senhas em um conjunto e verifica se a senha digitada pelo usuário
  está ou não neste conjunto para permitir ou proibir a entrada na residência.
'''

senhas = ['452012', '323233', '787910', '528917', '683524'];
senha = input("Digite a senha de acesso: ");
if senha in senhas:
  print("Acesso liberado");
else:
  print("Acesso negado!");