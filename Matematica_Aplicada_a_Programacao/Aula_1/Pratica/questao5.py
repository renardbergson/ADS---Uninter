"""  
  Em uma determinada disciplina, para compor a nota, foram realizadas duas atividades práticas e uma prova objetiva. 
  
  I - A primeira atividade prática corresponde a 20% da nota 
  II - A segunda atividade prática corresponde a 30% da nota  
  III - A prova objetiva corresponde a 50% da nota
  
  Sabendo que: 
  a - Se o estudante obtiver nota inferior a 30 está reprovado 
  b - Nota maior ou igual a 30 e menor do que 70 está em exame final 
  c - Nota maior ou igual a 70 está aprovado
  
  Faça um programa em Python onde são informadas as notas obtidas nas duas atividades práticas e na prova objetiva e é informada a nota obtida na disciplina e o resultado (reprovado, em exame final ou aprovado). 
  
  Considere a nota da disciplina com uma casa decimal.
"""

pratica1 = float(input("Digite a nota da Atividade Prática 1 (de 0 a 100): "));
pratica2 = float(input("Digite a nota da Atividade Prática 2: (de 0 a 100) "));
objetiva = float(input("Digite a nota da Prova Objetiva: (de 0 a 100) "));

print();
nota = (pratica1 * 0.20) + (pratica2 * 0.30) + (objetiva * 0.50);
print(f"Sua nota foi: {nota:.1f}");

if nota < 30:
  print();
  print("Aluno reprovado!");
elif nota >= 30 and nota < 70:
  print();
  print("Aluno classificado para exame final!");
else:
  print();
  print("Aluno aprovado...");