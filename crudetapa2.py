
# LISTA DE PRODUTOS
produtos = []


# FUNCAO PARA CADASTRAR
def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preco do produto: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")


# FUNCAO PARA VISUALIZAR
def visualizar_produtos():
    if len(produtos) > 0:

        print("\n===== PRODUTOS CADASTRADOS =====")

        for i in range(len(produtos)):
            print("\nProduto:", i + 1)
            print("Nome:", produtos[i]["nome"])
            print("Preco: R$", produtos[i]["preco"])
            print("Estoque:", produtos[i]["quantidade"])

    else:
        print("Nenhum produto cadastrado.")


# FUNCAO PARA ATUALIZAR
def atualizar_produto():
    if len(produtos) > 0:

        visualizar_produtos()

        numero = int(input("\nDigite o numero do produto: "))

        if numero >= 1 and numero <= len(produtos):

            indice = numero - 1

            produtos[indice]["nome"] = input("Novo nome: ")
            produtos[indice]["preco"] = float(input("Novo preco: R$ "))
            produtos[indice]["quantidade"] = int(input("Nova quantidade: "))

            print("Produto atualizado com sucesso!")

        else:
            print("Produto nao encontrado.")

    else:
        print("Nenhum produto cadastrado.")


# FUNCAO PARA EXCLUIR
def excluir_produto():
    if len(produtos) > 0:

        visualizar_produtos()

        numero = int(input("\nDigite o numero do produto: "))

        if numero >= 1 and numero <= len(produtos):

            produtos.pop(numero - 1)

            print("Produto excluido com sucesso!")

        else:
            print("Produto nao encontrado.")

    else:
        print("Nenhum produto para excluir.")


# PROGRAMA PRINCIPAL
opcao = 0

while opcao != 5:

    print("\n===== SISTEMA DE PRODUTOS =====")
    print("1 - Cadastrar produto")
    print("2 - Visualizar produtos")
    print("3 - Atualizar produto")
    print("4 - Excluir produto")
    print("5 - Sair")

    opcao = int(input("\nEscolha uma opcao: "))

    if opcao == 1:
        cadastrar_produto()

    elif opcao == 2:
        visualizar_produtos()

    elif opcao == 3:
        atualizar_produto()

    elif opcao == 4:
        excluir_produto()

    elif opcao == 5:
        print("Obrigado por utilizar o aplicativo!")

    else:
        print("Opcao invalida!")
