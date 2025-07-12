produtos = { "Mouse": 98.75,
            "Teclado": 125.65,
            "Monitor": 134.78,
            "Gabinete": 170.00,
            "HD Externo": 510.50,
            "Headset": 125.45 }
while True:
    produto = input("Informe o produto a pesquisar o preço ou fim para sair: ")
    if produto == "fim":
        break
    if produto in produtos:
        print(f"Produto {produto} custa {produtos[produto]}.")
    else:
        print(f"Produto {produto} não encontrado.")