'''
Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de pessoas. Este software deve ter o seguinte menu e opções:

1)	Cadastrar Livro
2)	Consultar Livro
1.	Consultar Todos 
2.	Consultar por Id
3.	Consultar por Autor
4.	Retornar ao menu
3)	Remover Livro
4)	Encerrar Programa

Elabore um programa em Python que: 

A.	Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 8];
B.	Deve-se implementar uma lista vazia com o nome de lista_livro e a variável id_global com valor inicial igual a 0 [EXIGÊNCIA DE CÓDIGO 2 de 8];
C.	Deve-se implementar uma função chamada cadastrar_livro(id) em que: [EXIGÊNCIA DE CÓDIGO 3 de 8];
a.	Pergunta nome, autor, editora do livro;
b.	Armazena o id (este é fornecido via parâmetro da função), nome, autor, editora dentro de um dicionário;
c.	Copiar o dicionário para dentro da lista_livro;
D.	Deve-se implementar uma função chamada consultar_livro() em que: [EXIGÊNCIA DE CÓDIGO 4 de 8];
a.	Deve-se perguntar qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Autor / 4. Retornar ao menu) e   printar a “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
i.	Se Consultar Todos, apresentar todos os livros com todos os seus dados cadastrados;
ii.	Se Consultar por Id, apresentar o livro específico com todos os seus dados cadastrados;
iii.	Se Consultar por Autor, apresentar o(s) livro(s) do autor com todos os seus dados cadastrados;
iv.	Se Retornar ao menu, deve-se retornar ao menu principal;
E.	Deve-se implementar uma função chamada remover_livro() em que: [EXIGÊNCIA DE CÓDIGO 5 de 8];
a.	Deve-se pergunta pelo id do colaborador a ser removido;
b.	Remover o livro da lista_livro;
F.	Deve-se implementar uma estrutura de menu no main em que: [EXIGÊNCIA DE CÓDIGO 6 de 8];
a.	Deve-se pergunta qual opção deseja (1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa)e executar o printar de “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 :
i.	Se Cadastrar Livro, acrescentar em um id_ global e chamar a função cadastrar_livro(id_ global);
ii.	Se Consultar Livro, chamar função consultar_livro();
iii.	Se Remover Livro, chamar função remover_livro();
iv.	Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
G.	Deve-se implementar uma lista de dicionários (uma lista contento dicionários dentro) [EXIGÊNCIA DE CÓDIGO 7 de 8];
H.	Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 8 de 8];
I.	Deve-se apresentar na saída de console uma mensagem de boas-vindas com o seu nome [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 6];
J.	Deve-se apresentar na saída de console um cadastro de 3 livros (sendo 2 deles no mesmo autor) [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 6];
K.	Deve-se apresentar na saída de console uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 3 de 6];
L.	Deve-se apresentar na saída de console uma consulta por código de um dos livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 4 de 6];
M.	Deve-se apresentar na saída de console uma consulta por setor em que 2 livros sejam do mesmo autor [EXIGÊNCIA DE SAÍDA DE CONSOLE 5 de 6];
N.	Deve-se apresentar na saída de console uma remoção de um dos livros seguida de uma consulta de todos os livros [EXIGÊNCIA DE SAÍDA DE CONSOLE 6 de 6];
'''

def menu_principal():
    global id_global

    while True:
        print()
        print('*****************************************************')
        print('-' * 19, 'MENU PRINCIPAL', '-' * 18)
        print('Digite o número da opção desejada:')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')
        print('3 - Remover Livro')
        print('4 - Sair')
        
        opcao = input('==> ')

        if opcao not in opcoes:
            print('Opção inválida!')
        else:
            if opcao == '1':
                id_global += 1
                cadastrar_livro(id_global)
                break
            elif opcao == '2':
                if len(lista_livros) == 0: # nenhum livro cadastrado
                    print()
                    print('Ainda não há nenhuma obra literária cadastrada!')
                    continue
                else:
                    consultar_livro()
                    break
            elif opcao == '3':
                if len(lista_livros) == 0: # nenhum livro cadastrado
                    print()
                    print('Ainda não há nenhuma obra literária cadastrada!')
                    continue
                else:
                    remover_livro()
                    break
            else: # opção 4 (sair)
                print()
                print('O programa foi encerrado.')
                break

def cadastrar_livro(id):
    global lista_livros
    print()
    print('*****************************************************')
    print('-' * 16, 'MENU CADASTRAR LIVRO', '-' * 15)
    print('ID do livro {}' .format(id))
    obra = input('Digite o nome da obra: ')
    autor = input('Digite o nome do autor: ')
    editora = input('Digite o nome da editora: ')

    dados = {
        'id': id,
        'nome': obra,
        'autor': autor,
        'editora': editora
    }

    lista_livros += [dados]
    print()
    print('A obra literária foi cadastrada com sucesso!')
    menu_principal()

def consultar_livro():
    while True:
        print()
        print('*****************************************************')
        print('-' * 16, 'MENU CONSULTAR LIVRO', '-' * 15)
        print('Digite o número da opção desejada:')
        print('1 - Consultar Todos os Livros')
        print('2 - Consultar Livro por ID')
        print('3 - Consultar Livro(s) por Autor')
        print('4 - Retornar')

        opcao = input('==> ')

        if opcao not in opcoes:
            print('Opção inválida!')
            continue
        else:
            if opcao == '1':
                print()
                print('-' * 20)
                for livro in lista_livros:
                    for i in livro:
                        print('● {}: {}' .format(i, livro[i]))
                    print()
                print('-' * 20)
                menu_principal()
                break
            elif opcao == '2':
                id = input('Digite o ID da obra: ')
                print()
                print('-' * 20)
                for livro in lista_livros:
                    if livro['id'] == int(id):
                        for i in livro:
                            print('● {}: {}' .format(i, livro[i]))
                        print()
                print('-' * 20)
                menu_principal()
                break
            elif opcao == '3':
                autor = input('Digite o nome do autor da obra: ')
                print()
                print('-' * 20)
                for livro in lista_livros:
                    if livro['autor'] == autor:
                        for i in livro:
                            print('● {}:{}' .format(i, livro[i]))
                        print()
                print('-' * 20)
                menu_principal()
                break
            else: # retornar (4)
                menu_principal()
                break

def remover_livro():
    print()
    print('*****************************************************')
    print('-' * 17, 'MENU REMOVER LIVRO', '-' * 16)

    if len(lista_livros) == 0:
        print('Ainda não há nenhuma obra literária cadastrada!')
        menu_principal()
    else:
        id = input('Digite o ID da obra a ser removida: ')
        
        for livro in lista_livros:
            if livro['id'] == int(id):
                lista_livros.remove(livro)
                print()
                print('A obra referenciada foi removida com sucesso!')
        menu_principal()

# INÍCIO DO FLUXO
opcoes = ('1', '2', '3', '4')
id_global = 0
lista_livros = []

print('Bem-vindo à biblioteca do Renard Bergson, RU: 3426934')
menu_principal()