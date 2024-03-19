'''
  Strings são imutáveis mas, podemos torná-las listas e alterá-las com o método list(), por exemplo
'''
s1 = list('Algoritmos')
print(s1) # print separado
s1[0] = 'a'
print(s1)
print(''.join(s1)) # print agrupado

# VERIFICANDO CARACTERES
s1 = 'Lógica de Programação e Algoritmos'
print(s1.startswith('Lógica')) # true
print(s1.endswith('Algoritmos')) # True
print(s1.endswith('algoritmos')) # false
print(s1.lower().endswith('algoritmos')) # true

# CONTANDO CARACTERES
s1 = 'Um pato, dois patos, três patos'
print(s1.lower().count('pato')) # 3

# QUEBRANDO STRINGS
s1 = 'Uma vaca, duas vacas, três vacas'
print(s1.split(' '))

# SUBSTITUINDO STRINGS
s1 = 'Um mafagafinho, dois mafagafinhos, três mafagafinhos'
print(s1.replace('mafagafinho', 'gatinho'))

# substituir uma quantidade de vezes específica
print(s1.replace('mafagafinho', 'gatinho', 1))