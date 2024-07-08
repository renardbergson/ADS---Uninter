'''
  QUESTÃO 2

  Construa um algorítmo, com base na cifra de César, para descriptografar mensagens que utilizam esse padrão
'''

from string import ascii_uppercase;

a = list(ascii_uppercase);
mc = input("Digite uma mensagem para descriptografar: ").upper();
m = "";

for l in mc:
  if l in a:
    i = ord(l) - 65;
    m += a[(i - 3) % 26].lower();
  else:
    # não faz nada se "l" não for uma letra do alfabeto (por exemplo, se for um espaço ou pontuação)
    l;
print(f'Mensagem descriptografada: {m}');