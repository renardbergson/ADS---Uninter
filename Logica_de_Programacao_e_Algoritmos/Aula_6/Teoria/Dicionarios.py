'''
  Estrutura de dados dinâmica, indexada por chaves, o que lembra um pouco os objetos JavaScript
'''

game = {
  'nome': 'Super Mario',
  'desenvolvedora': 'Nintendo',
  'ano': 1990
}

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])
print()

'''
  Métodos:

  values: obtém somente os dados
  keys: obtém somente as chaves
  items: obtém o par: chave:dado
'''

# VALUES
print(game.values())
print()
# ou
for i in game.values():
  print(i)
print()

# KEYS
print(game.keys())
print()
# ou
for i in game.keys():
  print(i)
print()

# ITEMS
print(game.items())
print()
# ou
for i, j in game.items():
  print('{} = {}' .format(i, j))

# LISTAS COM DICIONÁRIOS
games = []
game1 = {
  'nome': 'Super Mario',
  'videogame': 'Super Nintendo',
  'ano': 1990
}
game2 = {
  'nome': 'Zelda Ocarina of Time',
  'videogame': 'Nintendo 64',
  'ano': 1998
}
game3 = {
  'nome': 'Pokemon Yellow',
  'videogame': 'Game Boy',
  'ano': 1999
}
games = [game1, game2, game3]
print(games)
print()

# 2
game = {}
games = []

for i in range (1):
  game['nome'] = input('Digite o nome do game: ')
  game['videogame'] = input('Para qual plataforma ele foi lançado?: ')
  game['ano'] = input('Qual o ano de lançamento? ')

  games.append(game.copy())

print(games)

# DICIONÁRIOS COM LISTAS
games = {
  'nome': ['Super Mario', 'Zelda Ocarina of Time', 'Pokemon Yellow'],
  'videogame': ['Super Nintendo', 'Nintendo 64', 'Game Boy'],
  'ano': [1990, 1998, 1999]
}
print(games)
print()

# 2 ================================================
games = {'nome': [], 'videogame': [], 'ano': []}
for i in range (1):
  nome = input('Qual o nome do jogo?: ')
  videogame = input('Para qual videogame ele foi lançado?: ')
  ano = input('Qual o ano de lançamento?: ')

  games['nome'].append(nome)
  games['videogame'].append(videogame)
  games['ano'].append(ano)
print(games)