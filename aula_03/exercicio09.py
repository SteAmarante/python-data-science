# Crie dicionários com produtos e seus preços, e monte uma função que ao passar o
# produto ela retorne o preço desses produtos. Use except KeyError, para caso o
# usuário informe um produto incorreto. Finally para Consulta encerrada.

produtos = { "Mouse": 98.75,
            "Teclado": 125.65,
            "Monitor": 134.78,
            "Gabinete": 170.00,
            "HD Externo": 510.50,
            "Headset": 125.45 }

def passeProduto(produto):

    try:
        print(f"Produto {produto} custa {produtos[produto]}.")
    except:
        print(f"Produto {produto} não encontrado.")
    finally:
        print("Pesquisa finalizada!")


produto = input("Informe o produto a pesquisar o preço: ")
passeProduto(produto)