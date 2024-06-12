"""   
  Exercício com Conjunção (e), na qual todas as condições precisam ser satisfeitas
  
  Construa um algorítmo para calcular a média de um aluno, com base nos termos a seguir:

  a - Duas atividades pedagógicas APOL com peso de 15% (0.15) cada
  b - Uma prova objetiva com peso de 30%
  c - Uma atividade prática com peso de 40% (040)

  Resultados:
    - Se a média for menor do que 30, o aluno está reprovado
    - Se a média for maior ou igual a 30 e menor que 67 o estudante fará exame final
    - Se a média for maior ou igual a 67 e menor que 70, a média será arredondada e o aluno aprovado
    - Se a média for maior ou igual a 70, o aluno está aprovado
"""

apol1 = float(input("Digite a nota da apol 1: "));
apol2 = float(input("Digite a nota da apol 2: "));
provaObj = float(input("Digite a nota da prova objetiva: "));
ativPrat = float(input("Digite a nota da atividade prática: "));
media = (0.15 * apol1) + (0.15 * apol2) + (0.3 * provaObj) + (0.4 * ativPrat); 
# a média é igual ao peso vezes as notas

print(f'Sua média: {media: .0f}');

if media < 30:
  print("Reprovado!");
elif media >= 30 and media < 67:
  print("Em exame final");
elif media >= 67 and media <70:
  print("Aprovado por arredondamento");
else:
  print("Aprovado!");