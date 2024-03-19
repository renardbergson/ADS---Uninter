'''
  Possuem uma estrutura de dados dinâmica, ou seja, é possível adicionar ou remover items através de código. São representadas por colchetes, por isso, são SEMELHANTES aos arrays em JavaScript.
'''

# alterando itens
ingredientes = ['Pão', 'Ovo', 'Queijo']
ingredientes[2] = 'Mortadela'
print(ingredientes)

# inserindo itens ao final
mochila = ['Celular', 'Notebook']
mochila.append('Caderno')
print(mochila)

#inserindo itens em índices específicos
mochila.insert(1, 'Garrafa de água')
print(mochila)

# excluindo itens por índice
del mochila[1]
print(mochila)

# excluindo itens por referência
mochila.remove('Celular')
print(mochila)

# CÓPIANDO LISTAS 
# mesma referência
x = [1, 2, 3, 4]
y = x
y[3] = 5
print(x)
print(y) # ambas as listas são alteradas, Y é só uma referência de X

# cópia real
alpha = ['a', 'b', 'c']
beta = alpha[:]
beta[2] = 'd'
print(alpha)
print(beta)