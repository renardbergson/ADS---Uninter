'''
  Um dos primeiros algoritmos destinados à criptografia de mensagens foi a Cifra
  de César. É um algoritmo simples baseado na substituição de letras por outras a
  partir de uma troca de posições. 
  
  Utilizando uma troca pela letra que está QUATRO posições à frente, temos que a letra “a” é substituída pela letra “e”, a letra “b” é substituída pela letra “f” e assim por diante. 
  
  Considerando a mensagem “MAIS AMOR”, por meio do Python, qual é a respectiva forma criptografada utilizando a Cifra de César com a substituição descrita acima?
'''
from string import ascii_uppercase;
a = list(ascii_uppercase);
m = "MAIS AMOR".upper();
mc = "";

for l in m:
  if l in a:
    i = ord(l) - 65;
    mc += a[(i + 4) % 26];
  else:
    mc += l;

print(f"Forma criptografada da mensagem 'MAIS AMOR': {mc}");