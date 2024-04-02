'''
    notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

    Com base na lista fornecida, resolva as demandas a seguir:

    a - Encontre a maior nota
    b - Ordene a lista do maior para o menor
    c - A média das notas
'''

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# a
print('A maior nota encontrada foi: {}' .format(max(notas)))

# b
print('A lista de notas, da maior para a menor fica assim: {}' .format(sorted(notas))) 

# c
soma = 0
for i in notas:
    soma += i
    media = soma / len(notas)
print('A média das notas fornecidas é igual a: {}' .format(round(media, 1)))