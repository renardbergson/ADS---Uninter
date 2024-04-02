'''
Enunciado: Você foi contratado para desenvolver um sistema de cobrança de serviços de uma copiadora. Você ficou com a parte de desenvolver a interface com o funcionário.
A copiadora opera da seguinte maneira:

•	Serviço de Digitalização (DIG) o custo por página é de um real e dez centavos;
•	Serviço de Impressão Colorida (ICO) o custo por página é de um real; 
•	Serviço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos; 
•	Serviço de Fotocópia (FOT) o custo por página é de vinte centavos; 

•	Se número de páginas for menor que 20 retornar o número de página sem desconto;
•	Se número de páginas for igual ou maior que 20 e menor que 200 retornar o número de páginas com o desconto é de 15%;
•	Se número de páginas for igual ou maior que 200 e menor que 2000 retornar o número de páginas com o desconto é de 20%;
•	Se número de páginas for igual ou maior que 2000 e menor que 20000 retornar o número de páginas com o desconto é de 25%;
•	Se número de páginas for maior ou igual à 20000 não é aceito pedidos nessa quantidade de páginas;

♦	Para o adicional de encadernação simples (1) é cobrado um valor extra de 15 reais;
♦	Para o adicional de encadernação de capa dura (2) é cobrado um valor extra de 40 reais;

O valor final da conta é calculado da seguinte maneira:

total = servico * num_pagina + extra

Elabore um programa em Python que: 
 
A.	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 7];
B.	Deve-se implementar a função escolha_servico() em que: [EXIGÊNCIA DE CÓDIGO 2 de 7];
a.	Pergunta o servico desejado;
b.	Retorna o valor do serviço com base na escolha do usuário;
c.	Repete a pergunta do item B.a se digitar serviço se digitar uma opção diferente de: dig/ico/ibo/fot;
C.	Deve-se implementar a função num_pagina() em que: [EXIGÊNCIA DE CÓDIGO 3 de 7];
a.	Pergunta o número de páginas;
b.	Retorna o número de páginas com desconto seguindo a regra do enunciado;
c.	Repete a pergunta do item C.a se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico)
D.	Deve-se implementar a função servico_extra() em que: [EXIGÊNCIA DE CÓDIGO 4 de 7];
a.	Pergunta pelo serviço adicional;
b.	Retornar uma das opções de adicional 
c.	Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0;
E.	Deve-se implementar o total a pagar na parte do main conforme o enunciado [EXIGÊNCIA DE CÓDIGO 5 de 7];
F.	Deve-se implementar try/except [EXIGÊNCIA DE CÓDIGO 6 de 7];
G.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 7 de 7];
H.	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
I.	Deve-se apresentar na saída de console um pedido no qual o usuário errou a opção de serviço [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4];
J.	Deve-se apresentar na saída de console um pedido no qual o usuário digitou ultrapassou no número de páginas [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
K.	Deve-se apresentar na saída de console um pedido com opção de serviço, número de páginas e serviço extra válidos [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];
'''

def moeda(valor):
    locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
    formatado = locale.currency(valor)
    return formatado

def escolha_servico():
    print()
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')

    while True:
        print()
        servico = input('Digite a sigla do serviço desejado: ')
        if servico not in servicos:
            print('Opção Inválida!')
            continue
        else:
            if servico == 'DIG' or servico == 'dig':
                print('Serviço: Digitalização')
                print('Preço: R$ 1,10 por página')
                num_pagina(1.10)
                break
            elif servico == 'ICO' or servico == 'ico':
                print('Serviço: Impressão Colorida')
                print('Preço: R$ 1,00 por página')
                num_pagina(1)
                break
            elif servico == 'IPB' or servico == 'ipb':
                print('Serviço: Impressão Preto e Branco')
                print('Preço: R$ 0,40 por página')
                num_pagina(0.40)
                break
            else: # FOT ou fot (fotocópia)
                print('Serviço: Fotocópia')
                print('Preço: R$ 0,20 por página')
                num_pagina(0.20)
                break

def num_pagina(preco_servico):
    global total
    
    while True:
        try:
            print()
            numPagina = int(input('Digite a quantidade de páginas: '))
        except:
            # erro (não numérico)
            print('Comando inválido. Digite um número inteiro!')
            continue
        else:
            # sucesso
            if numPagina >= 20000:
                # quantidade acima do permitido
                print('Desculpe, não atendemos a uma quantidade de páginas igual ou superior a 20 mil.')
                print('Por favor, insira novamente a quantidade de páginas para o serviço.')
                continue
            else:
                # quantidade permitida
                _total = preco_servico * numPagina

                if numPagina < 20:
                    # sem desconto
                    total += _total 
                    print('O valor deste serviço é: {}' .format(moeda(_total)))
                    break
                elif numPagina >= 20 and numPagina < 200:
                    # desconto de 15%
                    desconto = 15 / 100 * _total 
                    _total -= desconto
                    total += _total
                    print('Parabéns. Você ganhou um desconto de 15%. O valor deste serviço, com o desconto é: {}' .format(moeda(_total)))
                    break
                elif numPagina >= 200 and numPagina < 2000:
                    # desconto de 20%
                    desconto = 20 / 100 * _total 
                    _total -= desconto
                    total += _total
                    print('Parabéns. Você ganhou um desconto de 20%. O valor deste serviço, com o desconto é: {}' .format(moeda(_total)))
                    break
                else: # igual ou maior que 2.000 (menor que 20.000)
                    # desconto 25%
                    desconto = 25 / 100 * _total 
                    _total -= desconto
                    total += _total
                    print('Parabéns. Você ganhou um desconto de 25%. O valor deste serviço, com o desconto é: R$ {}' .format(moeda(_total)))
                    break
    if numPagina:
        servico_extra(preco_servico, numPagina, _total)

def servico_extra(preco, paginas, aPagar):
    global total
    custoExtra = 0

    while True:
        print()
        print('Deseja solicitar algum serviço extra?')
        print()
        print('0 - Finalizar')
        print('1 - Encadernação Simples - R$ 10,00')
        print('2 - Encadernação Capa Dura - R$ 25,00')
        print()
        
        opcao = input('Digite a opção desejada: ')

        if opcao == '0':
            break
        elif opcao == '1':
            custoExtra += 10
            total += custoExtra
            break
        elif opcao == '2':
            custoExtra += 25
            total += custoExtra
            break
        else:
            continue
    print()
    print('Obrigado pela preferência!')
    print('Custo: {}' .format(moeda(preco)))
    print('Quantidade de páginas: {}' .format(paginas))
    print('Preço: {}' .format(moeda(aPagar)))
    print('Adicionais: {}' .format(moeda(custoExtra)))
    print('VALOR TOTAL: {}' .format(moeda(total)))
    print()

# Fluxo Principal
import locale

servicos = ('DIG', 'dig', 'ICO', 'ico', 'IPB', 'ipb', 'FOT', 'fot')
total = 0

print('Bem-vindo à gráfica do Renard Bergson, RU: 3426934')

escolha_servico()