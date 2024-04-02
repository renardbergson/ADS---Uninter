'''
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:

•	Tamanho P de Cupuaçu (CP) custa R$ 9.00 e o Açaí (AC) custa R$ 11.00;
•	Tamanho M de Cupuaçu (CP) custa R$ 14.00 e o Açaí (AC) custa R$ 16.00;
•	Tamanho G de Cupuaçu (CP) custa R$ 18.00 e o Açaí (AC) custa R$ 20.00;
Elabore um programa em Python que: 
 
A.	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8];
B.	Deve-se implementar o input  do sabor (CP/AC) e o print “Sabor inválido. Tente novamente" se o usuário entrar com valor diferente de CP e AC [EXIGÊNCIA DE CÓDIGO 2 de 8];
C.	Deve-se implementar o input  do tamanho (P/M/G) e o print “Tamanho inválido. Tente novamente" se o usuário com entra valor diferente de P,M ou G [EXIGÊNCIA DE CÓDIGO 3 de 8];
D.	Deve-se implementar if/elif com cada uma das combinações de sabor e tamanho do enunciado [EXIGÊNCIA DE CÓDIGO 4 de 8];
E.	Deve-se implementar um acumulador para somar os valores dos pedidos [EXIGÊNCIA DE CÓDIGO 5 de 8];
F.	Deve-se implementar o input com a pergunta: “Deseja pedir mais alguma coisa?”. Se sim repetir a partir do item B, senão encerrar o programa executar o print do acumulador [EXIGÊNCIA DE CÓDIGO 6 de 8];
G.	Deve-se implementar as estruturas de while, break, continue (todas elas) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
I.	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 4];
J.	Deve-se apresentar na saída de console um pedido em que o usuário errou o sabor [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 4]; 
K.	Deve-se apresentar na saída de console um pedido em que o usuário errou o tamanho [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 4];
L.	Deve-se apresentar na saída de console um pedido com duas opções sabores diferentes e com tamanhos diferentes [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 4];  
'''

print('Bem-vindo à loja de gelados do Renard Bergson, RU: 3426934')
print()
print('{} Cardápio {}' .format('-' * 19, '-' * 21))
print('------| Tamanho | Cupuaçu (CP) | Açaí (AC) |------')
print('------|    P    |   R$ 10,00   |  R$ 12,00 |------')
print('------|    M    |   R$ 15,00   |  R$ 17,00 |------')
print('------|    G    |   R$ 19,00   |  R$ 21,00 |------')
print()
produtos = ('CP', 'cp', 'AC', 'ac')
tamanhos = ('P', 'p', 'M', 'm', 'g', 'G')
total = 0
texto = 'Deseja pedir mais alguma coisa? (S/N): '

def carrinho(preco, produto, tamanho):
    global total
    print()
    print('Você pediu {}, tamanho {} (R$ {},00)' .format(produto, tamanho, preco))
    total += preco
    while True:
        pergunta = input(texto)
        if pergunta == 'S' or pergunta == 's':
            print()
            return True
        elif pergunta == 'N' or pergunta == 'n':
            return False
        else:
            continue
while True:
    # Seleção
    produto = input('Digite o sabor do produto desejado (CP/AC): ')
    if produto not in produtos:
        print('Produto inválido. Tente novamente! \n')
        continue
    tamanho = input('Digite o tamanho desejado (P/M/G): ')
    if tamanho not in tamanhos:
        print('Tamanho inválido. Tente novamente! \n')
        continue
    # Compra
    if produto == 'CP' or produto == 'cp':
        if tamanho == 'P' or tamanho == 'p':
            compra = carrinho(9, 'CUPUAÇU', 'P')
            if compra:
                continue
            else:
                break
        elif tamanho == 'M' or tamanho == 'm':
            compra = carrinho(14, 'CUPUAÇU', 'M')
            if compra:
                continue
            else:
                break
        else: # Cupuaçu tamanho G
            compra = carrinho(18, 'CUPUAÇU', 'G')
            if compra:
                continue
            else:
                break
    else: # Açaí
        if tamanho == 'P' or tamanho == 'p':
            compra = carrinho(11, 'AÇAÍ', 'P')
            if compra:
                continue
            else:
                break
        elif tamanho == 'M' or tamanho == 'm':
            compra = carrinho(16, 'AÇAÍ', 'M')
            if compra:
                continue
            else:
                break
        else: # Açaí tamanho G
            compra = carrinho(20, 'AÇAÍ', 'G')
            if compra:
                continue
            else:
                break
# Checkout
print()
print('Obrigado pela preferência!')
print('Valor total a pagar: R$ {},00' .format(total))