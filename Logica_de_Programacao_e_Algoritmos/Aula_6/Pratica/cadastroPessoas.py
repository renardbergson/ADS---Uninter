'''
    Crie um programa para ler as seguintes informações das pessoas:
    a - Nome
    b - Ano de nascimento
    c - Sexo

    Armazene os dados em um dicionário com listas
    Ao encerrar o cadastro, apresente:
    1 - O total de cadastros realizados
    2 - A média de idade dos cadastrados
    3 - Uma lista de mulheres com menos de 30 anos
    4 - Uma lista de homens com idade acima da média
'''

cadastro = {
    'nome': [],
    'ano': [],
    'sexo': [],
}

print('-- Programa para Cadastro de Pessoas Físicas -- \n')

while True:
    inicio = input('Deseja prosseguir e cadastrar um usuário? [S/N]: ')
    print()

    if inicio in 'Nn':
        break
    elif inicio in 'Ss':
        nome = input('Digite o nome da pessoa: ')
        ano = int(input('Digite o ano de nascimento: '))
        sexo = input('Digite o sexo [M/F]: ')
        
        cadastro['nome'].append(nome)
        cadastro['ano'].append(ano)
        cadastro['sexo'].append(sexo.upper())
    else:
        continue

if cadastro['nome']:
    print(cadastro)
    print('Um total de {} pessoas foram cadastradas.' .format(len(cadastro['nome'])))