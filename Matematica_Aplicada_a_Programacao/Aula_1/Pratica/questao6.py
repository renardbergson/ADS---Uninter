"""  
  QUESTÃO 6

  Em uma empresa, a entrada em um determinado setor é liberada após o funcionário digitar uma determinada senha. Sabendo que uma das senhas é 705080 e que a outra senha é 999999, faça um programa em Python onde o usuário digita uma senha. Se a senha estiver correta, aparece a mensagem que a entrada está liberada. Caso contrário, a mensagem é de que a entrada não está autorizada.
"""

senha = input("Digite senha de acesso A ou B: ");

if senha == "705080" or senha == "999999":
  print("Acesso liberado...");
else:
  print("Acesso negado!");