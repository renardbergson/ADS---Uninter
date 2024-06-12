"""
  Exercício com Disjunção (ou), na qual pelo menos uma condição precisa ser satisfeita, ou todas

  Escreva o seguinte algorítmo:

  I - Se a pessoa apresentar RG, tem entrada liberada
  II - Se apresentar CPF, tem entrada liberada
  III - Se apresentar ambos, também tem entrada liberada
  IV - Se não apresentar nenhum, tem a entrada negada
"""

rg = input("Está com o RG em mãos? (s/n): ");
cpf = input("Está com o CPF em mãos? (s/n): ");

if (rg == 's' or cpf == 's'):
  print("Entrada liberada...");
else:
  print("Acesso negado!");