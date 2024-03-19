'''
  Imagine uma situação na qual você deve realizar o cadastro de uma lista de compras em um sistema. Cada produto deverá ser regustrado com nome, quantidade e valor unitário.
'''

item = []
mercado = []

for i in range (3):
  item.append(input('Digite o nome do item: '))
  item.append(input('Digite a quantidade: '))
  item.append(input('Digite o valor unitário: '))
  mercado.append(item[:]) # copiamos, caso contrário, ao zerar "item", "mercado" também ficará vazio
  item.clear()
print(mercado)