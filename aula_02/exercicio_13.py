# Remova o produto 2 do dicionário e mostre o dicionário atualizado.

# Dicionário original
produtos = {
    "Produto 1": 10.50,
    "Produto 2": 25.90,
    "Produto 3": 7.30
}

# Remover o Produto 2
del produtos["Produto 2"]

# Mostrar dicionário atualizado
print("Dicionário atualizado:")
print(produtos)

print("\nProdutos restantes:")
for produto, preco in produtos.items():
    print(f"{produto}: R${preco:.2f}")
