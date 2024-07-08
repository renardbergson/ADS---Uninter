'''
  CIFRA / CRIPTOGRAFIA DE CÉSAR

  A criptografia de César, ou cifra de César, é uma técnica de criptografia muito simples e antiga, na qual é feita uma substituição monoalfabética, de modo que cada letra é substituída por uma letra que se encontra 3 posições à frente no alfabeto. O alfabeto é considerado cíclico, ou seja, após Z, volta-se a A.

  QUESTÃO 1

  Construa um algorítmo que utilize a cifra de César para criptografar uma mensagem. 
  Detalhe: a cifra de César tradicionalmente só lida com letras do alfabeto, mas podemos estendê-la para incluir números. Para fazer isso, precisamos definir uma forma de manipular os números de forma semelhante às letras. Uma abordagem comum é tratar números como parte de um ciclo de 10 (0-9)
'''

from string import ascii_uppercase;
a = list(ascii_uppercase);
# Inicialmente, o código importa a sequência de letras do alfabeto (A a Z) da biblioteca "string" e a converte em uma lista, atribuindo-a à variavel "a"
m = input("Digite uma mensagem para criptografar: ").upper();
mc = "";
# Depois, o código solicita ao usuário que digite uma mensagem e a converte para letras maiúsculas, armazenazenando-a na variável "m". A variável "mc" é inicializada como uma string vazia e será usada para construir a mensagem criptografada

for l in m:
  # Este loop percorre cada caractere na mensagem "m", atribuindo cada elemento à variável "l". A função ord(l) retorna o valor desses elementos na tabela ASCII, lembrando que, neste caso todas estarão já em formato maiúsculo
  # Do valor obtido da tabela ASCII para cada elemento, subtraimos 65, visto que, "A" na referida tabela equivale a 65, deste modo, obtemos um conjunto com 26 caracteres (0 a 25), onde A é 0, B é 1, etc
  if l in a:
    # Se for "l" for uma letra do alfabeto, será adicionada à variável string "mc". 
    # Cada letra será substituida por uma de 3 posições à frente, usando o operador de módulo vinte e seis (alfabeto tem 26 letras), para garantir que o índice volte ao início do alfabeto, se passar de Z
    i = ord(l) - 65;
    mc += a[(i + 3) % 26];
  else:
    # não faz nada se "l" não for uma letra do alfabeto (por exemplo, se for um espaço ou pontuação)
    l;
print(f'Mensagem criptografada: {mc}');