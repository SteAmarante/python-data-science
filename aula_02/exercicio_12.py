# Crie um dicionário com 3 produtos e seus preços. Mostre o preço do produto 1.

# Dicionário com produtos e preços
produtos = {
    "Produto 1": 10.50,
    "Produto 2": 25.90,
    "Produto 3": 7.30
}

# Mostrar o preço do Produto 1
print("O preço do Produto 1 é:", produtos["Produto 1"])


# Mostrar o preço de todos os Produtos
print("\nTodos os produtos e preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R${preco:.2f}")
