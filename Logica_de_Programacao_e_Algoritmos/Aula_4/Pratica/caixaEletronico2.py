'''
  Repita o exercício do caixa eletrônico!
  Adapte o algoritmo para que seja considerado também certa quantidade de cédulas de cada tipo presentes dentro da máquina.
  Verifique também se é possível sacar o valor digitado, levando em consideração o valor total presente na máquina. 
'''

valor = int(input('Digite um valor inteiro em R$ o qual você deseja sacar: '))

cedulas_de_100_disponiveis = 5
cedulas_de_50_disponiveis = 8
cedulas_de_20_disponiveis = 16
cedulas_de_10_disponiveis = 27
cedulas_de_5_disponiveis = 11
cedulas_de_1_disponiveis = 32

saldo = (100 * cedulas_de_100_disponiveis) + (50 * cedulas_de_50_disponiveis) + (20 * cedulas_de_20_disponiveis) + (10 * cedulas_de_10_disponiveis) + (5 * cedulas_de_5_disponiveis) + (1 * cedulas_de_1_disponiveis) # R$ 1.577,00

""" 
  PASSOS:

  1 - Verificar se a máquina pode atender à demanda do saque
  2 - Verificar se o valor bate com o valor da cédula e se há cedulas desse tipo disponíveis
  3 - Verificar quantas cédulas desse tipo serão necessárias para abater todo o valor ou boa parte dele
  4 - Verificar quantas cédulas desse tipo podem ser entregues, de acordo com a quantidade disponível no caixa
  5 - Encontrar o desconto a ser aplicado, se a quantidade de cédulas disponíveis não suprir a demanda
"""

while True:
  if (valor <= saldo): # se houver saldo
    # 100
    if valor >= 100 and cedulas_de_100_disponiveis: # a cédula cabe no valor? o valor exceder a quantidade?
      cedulas_necessarias = valor // 100
      
      if cedulas_necessarias > cedulas_de_100_disponiveis: # não há cédulas de 100 suficientes
        cedulas_que_faltam = cedulas_necessarias - cedulas_de_100_disponiveis
        cedulas_a_sacar = cedulas_necessarias - cedulas_que_faltam # cédulas pro usuário
        valor_restante = valor - cedulas_a_sacar * 100 # valor não atendido pelas cédulas

        valor = valor_restante
        print('Será necessário {} cédula(s) de CEM reais.' .format(cedulas_a_sacar))
      else: # há cédulas de 100 suficientes
        desconto = cedulas_necessarias * 100
        valor -= desconto
        print('Será necessário {} cédula(s) de CEM reais.' .format(cedulas_necessarias))
      if not valor:
        break
    # 50
    if valor >= 50 and cedulas_de_50_disponiveis: # a cédula cabe no valor? o valor exceder a quantidade?
      cedulas_necessarias = valor // 50
      
      if cedulas_necessarias > cedulas_de_50_disponiveis: # não há cédulas de 50 suficientes
        cedulas_que_faltam = cedulas_necessarias - cedulas_de_50_disponiveis
        cedulas_a_sacar = cedulas_necessarias - cedulas_que_faltam # cédulas pro usuário
        valor_restante = valor - cedulas_a_sacar * 50 # valor não atendido pelas cédulas

        valor = valor_restante
        print('Será necessário {} cédula(s) de CINQUENTA reais.' .format(cedulas_a_sacar))
      else: # há cédulas de 50 suficientes
        desconto = cedulas_necessarias * 50
        valor -= desconto
        print('Será necessário {} cédula(s) de CINQUENTA reais.' .format(cedulas_necessarias))
      if not valor:
        break
    # 20
    if valor >= 20 and cedulas_de_20_disponiveis: # a cédula cabe no valor? o valor exceder a quantidade?
      cedulas_necessarias = valor // 20
      
      if cedulas_necessarias > cedulas_de_20_disponiveis: # não há cédulas de 20 suficientes
        cedulas_que_faltam = cedulas_necessarias - cedulas_de_20_disponiveis
        cedulas_a_sacar = cedulas_necessarias - cedulas_que_faltam # cédulas pro usuário
        valor_restante = valor - cedulas_a_sacar * 20 # valor não atendido pelas cédulas

        valor = valor_restante
        print('Será necessário {} cédula(s) de VINTE reais.' .format(cedulas_a_sacar))
      else: # há cédulas de 20 suficientes
        desconto = cedulas_necessarias * 20
        valor -= desconto
        print('Será necessário {} cédula(s) de VINTE reais.' .format(cedulas_necessarias))
      if not valor:
        break
    # 10
    if valor >= 10 and cedulas_de_10_disponiveis: # a cédula cabe no valor? o valor exceder a quantidade?
      cedulas_necessarias = valor // 10
      
      if cedulas_necessarias > cedulas_de_10_disponiveis: # não há cédulas de 10 suficientes
        cedulas_que_faltam = cedulas_necessarias - cedulas_de_10_disponiveis
        cedulas_a_sacar = cedulas_necessarias - cedulas_que_faltam # cédulas pro usuário
        valor_restante = valor - cedulas_a_sacar * 10 # valor não atendido pelas cédulas

        valor = valor_restante
        print('Será necessário {} cédula(s) de DEZ reais.' .format(cedulas_a_sacar))
      else: # há cédulas de 10 suficientes
        desconto = cedulas_necessarias * 10
        valor -= desconto
        print('Será necessário {} cédula(s) de DEZ reais.' .format(cedulas_necessarias))
      if not valor:
        break
    # 5
    if valor >= 5 and cedulas_de_5_disponiveis: # a cédula cabe no valor? o valor exceder a quantidade?
      cedulas_necessarias = valor // 5
      
      if cedulas_necessarias > cedulas_de_5_disponiveis: # não há cédulas de 5 suficientes
        cedulas_que_faltam = cedulas_necessarias - cedulas_de_5_disponiveis
        cedulas_a_sacar = cedulas_necessarias - cedulas_que_faltam # cédulas pro usuário
        valor_restante = valor - cedulas_a_sacar * 5 # valor não atendido pelas cédulas

        valor = valor_restante
        print('Será necessário {} cédula(s) de CINCO reais.' .format(cedulas_a_sacar))
      else: # há cédulas de 5 suficientes
        desconto = cedulas_necessarias * 5
        valor -= desconto
        print('Será necessário {} cédula(s) de CINCO reais.' .format(cedulas_necessarias))
      if not valor:
        break
    # 1
    if valor >= 1 and cedulas_de_1_disponiveis: # pagar o restante com cédulas de 1 real
      cedulas_necessarias = valor
      
      print('Será necessário {} cédula(s) de UM real.' .format(cedulas_necessarias))
      if not valor:
        break
  else: # saldo insuficiente
    print('Desculpe! Não é possível sacar o valor digitado. Tente novamente com outro valor.')
  break
  