"""  
  Para a liberação de um financiamento imobiliário, uma construtora exige que: 

  a - a renda mensal líquida mínima seja maior ou igual a R$ 8.500,00 e 
  b - que o comprometimento com outros financiamentos ou empréstimos não ultrapasse 20% da renda mensal líquida
  
  Utilizando o Python, faça um programa que informe se o financiamento será liberado ou não com base na renda mensal líquida e no total de outros financiamentos ou empréstimos por parte do cliente.
"""

renda = float(input("Digite a sua renda líquida mensal. (Ex.: 8500): "));
comprometimento = float(input("Quanto você paga por mês de financiamentos ou empréstimos? (Ex.: 1200): "));

if (renda >= 8500) and (comprometimento <= 0.2 * renda):
  print("Seu financiamento foi liberado!");
else:
  print("Financiamento negado...");