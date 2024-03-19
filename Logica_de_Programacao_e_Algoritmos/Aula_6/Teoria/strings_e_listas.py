# Strings dentro de listas
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila[0][0]) # Dupla Indexação (podemos acessar ainda mais itens aninhados)
print()

# percorrendo listas de strings com laços
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for item in mochila:
  for letra in item: # itens
    print(letra) # letras
print()

# percorrendo listas de strings com laços em range
mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
for i in range(0, len(mochila), 1):
  for j in range(0, len(mochila[i]), 1):
    print(mochila[i][j])