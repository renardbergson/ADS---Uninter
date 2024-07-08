'''
  Na criptografia RSA (Rivest-Shamir-Adleman), as letras são substituídas por números de dois dígitos. O Python possui uma biblioteca destinada à criptografia RSA. Considerando a palavra “mensagem”, qual é a respectiva forma criptografada?

  A chave privada é de conhecimento somente do remetente
  A chave pública é de conhecimento do destinatário
'''
import rsa;
chavePublica, chavePrivada = rsa.newkeys(512);
m = "mensagem";
mc = rsa.encrypt(m.encode(), chavePublica);
md = rsa.decrypt(mc, chavePrivada).decode();

print();
print("Mensagem original:", m);
print();

print("Mensagem criptografada:", mc);
print();

print("Mensage descriptografada:", md);
print();