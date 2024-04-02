'''
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar desconto maiores conforme o valor total da compra conforme a seguinte listagem:

•	Se valor total da compra for menor que R$ 2500.00 o desconto será de 0%;
•	Se valor total da compra for igual ou maior que R$ 2500.00 e menor que R$ 6000.00 o desconto será de 4%;
•	Se valor total da compra for igual ou maior que R$ 6000.00 e menor que R$ 10000.00 o desconto será de 7%;
•	Se valor total da compra for igual ou maior que R$ 10000.00 o desconto será de 11%;

Elabore um programa em Python que:
A.	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome e RU [EXIGÊNCIA DE CÓDIGO 1 de 6];
B.	Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6];
C.	Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
D.	Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6];
E.	Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
F.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
G.	Deve-se apresentar na saída de console uma mensagem de boas-vindas com seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
H.	Deve-se apresentar na saída de console um pedido recebendo desconto (valor total sem desconto acima de R$ 2500.00) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2];  
'''

print('Bem-vindo à loja do Renard Bergson, RU: 3426934 \n')
unidade = float(input('Digite o valor unitário do produto: '))
quantidade = int(input('Digite a quantidade desejada: '))
total = unidade * quantidade
print()
if total < 2500:
    print('O valor total a pagar equivale a R$ {}' .format(total))
    print('Não há desconto disponível para o valor obtido.')
elif total >= 2500 and total < 6000:
    desconto = 4 / 100 * total
    print('O valor total sem desconto equivale a R$ {}' .format(total))
    print('Com um desconto de 4% você pagará o total de R$ {}' .format(total - desconto))
elif total >= 6000 and total < 10000:
    desconto = 7 / 100 * total
    print('O valor total sem desconto equivale a R$ {}' .format(total))
    print('Com um desconto de 7% você pagará o total de R$ {}' .format(total - desconto))
else: # total igual ou maior que R$ 10 mil
    desconto = 11 / 100 * total
    print('O valor total sem desconto equivale a R$ {}' .format(total))
    print('Com um desconto de 11% você pagará o total de R$ {}' .format(total - desconto))