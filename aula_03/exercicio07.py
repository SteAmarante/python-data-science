# Crie uma função lista_compras(**produtosValor) que receba uma lista de compras
# (produtos e valor) e imprima-os de forma formatada junto com o vlaor total da
# compra.

def lista_compras(**produtosValor):
    """
    Recebe uma lista de compras com os produtos e seus respectivos valores,
    imprime cada item formatado e o valor total da compra.
    """
    total = 0
    print("🛒 Lista de Compras: ")
    for produto, valor in produtosValor.items():
        print(f"- {produto}: R$ {valor:.2f}")
        total += valor
    print(f"\n💰 Total da compra: R$ {total:.2f}")

lista_compras(Pao=6.70, Ovo=12.99, Iorgute=6.50, Leite=5.99, Banana=6.90)

