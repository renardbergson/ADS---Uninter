# Conversão: DECIMAL x BINÁRIO
# Em python, temos a função "bin()"
decimal = 25;
binario = bin(decimal);
print(binario); # 0b11001 (os dois primeiros dígitos indicam apenas a base binária, sendo o número, de fato, o que vem em seguida)
print(binario[2:]); # 11001 (do índice 2 em diante)

# Escreva um algoritmo com input para conversão de decimal para binário
numeroConverter = int(input("Digite um número inteiro para mostrá-lo em base binária: "));
print(f'O número binário correspondente é: {bin(numeroConverter)[2:]}');

# Conversão: DECIMAL x HEXADECIMAL
# Em python, temos a função "hex()"
decimal2 = 11868;
hexadecimal = hex(decimal2);
print(hexadecimal); # 0x2e5c (os dois primeiros dígitos indicam apenas a base hexadecimal, sendo o número, de fato, o que vem em seguida)
print(hexadecimal[2:]); # 2e5c (do índice 2 em diante)

# Escreva um algoritmo com input para conversão de decimal para hexadecimal
numeroConverter2 = int(input("Digite um número inteiro para mostrá-lo em base hexadecimal: "));
print(f'O número hexadecimal correspondente é: {hex(numeroConverter2)[2:]}');

# CONSTRUINDO NOSSO PRÓPRIO ALGORÍTMO DE CONVERSÃO DE BASE
# Nos exemplos anteriores, usamos algorítmos prontos para converter de uma base numérica para outra. Construa um algorítmo que faça a conversão DECIMAL x BINÁRIO (divisões sucessivas por 2)
numero = 2024;
_binario = "";

while numero > 0:
  _binario += str( numero % 2 ); # o símbolo "%" considera o resto de uma divisão
  numero //= 2; # o símbolo "//" considera a parte inteira de uma divisão
print(f"O número binário correspondente, derivado do algorítmo que criamos é: {_binario[::-1]}"); # mostra o número de trás pra frente