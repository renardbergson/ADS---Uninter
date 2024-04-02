'''
    Dada uma lista contendo as notas de alunos em uma disciplina, escreva uma expressão para:

    notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
    
    a - Encontrar quantos alunos tiraram a nota 7
    b - Alterar a última nota para 4
'''

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# a
print('{} alunos tiraram a nota 7!' .format(notas.count(7)))

# b
notas[-1] = 4
print(notas)