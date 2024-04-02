'''
    Crie uma tupla com 10 nomes. 
    Encontre dentro dessa tupla as vogais de cada palavra. 
    Faça um print na tela com o nome da palavra e as suas respectivas vogais.
'''

nomes = ('Renard', 'Esdras', 'Asriel', 'Jailes', 'Miguel')

for nome in nomes:
    print('\n Nome: {} - Vogais: ' .format(nome.upper()), end='')

    for letra in nome:
        if letra.lower() in 'aeiou':
            print(letra.upper() + ',', end=' ')