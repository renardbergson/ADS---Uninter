'''
  São strings inseridas dentro do nosso código Python que explicam o seu funcionamento.
  Precisam ser inseridas a partir da primeira linha de definição de uma função.
  São obtidas através do comando help()
'''

def soma (x = 0, y = 0, z = 0):
  '''
    Retorna a soma de até 3 valores numéricos quaisquer. 
    Todos os parâmetros são opcionais.

    x: valor numérico (opcional)
    y: valor numérico (opcional)
    z: valor numérico (opcional)
  '''

  return x + y + z


print(soma(3,2))
help(soma)