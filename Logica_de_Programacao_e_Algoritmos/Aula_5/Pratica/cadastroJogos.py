'''
  Escreva um algoritmo que permita cadastrar jogos, informando o nome e a qual plataforma ele pertence. Para isso, crie um menu de opções contendo:

  1 - Cadastrar novo item
  2 - listar os itens cadastrados
  3 - Sair

  Crie pelo menos uma função para cada opção do menu (cadastrar, sair)
  Armazene todos os dados em um arquivo de texto, que deve ser salvo em disco e manter os dados cadastrados
'''

def valida_int (pergunta, min, max):
  x = int(input(pergunta))
  while x < min or x > max:
    x = int(input(pergunta))
  return x

def existeArquivo (nomeArquivo):
  try:
    a = open(nomeArquivo, 'rt') # r = read, t = txt
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True
  
def abrirArquivo (nomeArquivo):
  try:
    a = open(nomeArquivo, 'rt') # r = read, t = txt
  except: 
    # caso dê erro
    print('Erro ao abrir o arquivo de registro!')
  else:
    # caso dê certo
    print(a.read())
  finally:
    # sempre será executado, com erro ou não
    a.close()
  
def criaArquivo (nomeArquivo):
  try:
    a = open(nomeArquivo, 'wt+') # w = write, t = txt, + = read and write
    a.close()
  except:
    print('Erro na criação do arquivo... \n')
  else:
    print('O arquivo para inserção {} foi criado com sucesso! \n' .format(nomeArquivo))

def cadastrarJogo (nomeArquivo, nomeJogo, plataforma):
  try:
    a = open(nomeArquivo, 'at') # a = write preserving previous content, t = txt
  except:
    print('Erro ao abrir o arquivo!')
  else:
    a.write('{} - {} \n' .format(nomeJogo, plataforma))
  finally:
    a.close()

# Programa Principal
arquivo = 'games.txt'

if existeArquivo(arquivo):
  print('Abrindo arquivo {}... \n' .format(arquivo))
else:
  print('Arquivo para registro não encontrado. Criando o arquivo {}...' .format(arquivo))
  criaArquivo(arquivo)

while True:
  print()
  print('MENU')
  print('1 - Cadastrar novo item')
  print('2 - Listar cadastros')
  print('3 - Sair')

  print()
  op = valida_int('Digite o número da opção desejada: ', 1, 3)
  print()

  if op == 1:
    print()
    nomeDoJogo = input('Digite o nome do jogo: ')
    plataforma = input('Digite a plataforma que roda o game: ')
    cadastrarJogo(arquivo, nomeDoJogo, plataforma)
  elif op == 2:
    abrirArquivo(arquivo)
  elif op == 3:
    print('Ok. O programa foi encerrado!')
    break