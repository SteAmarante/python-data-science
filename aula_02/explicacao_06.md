Dicionários

Dicionários são estruturas de dados similares às listas, porém, com
propriedades de acesso diferentes. Um dicionário consiste em um
conjunto de chaves e valores.
Sintaxe:

dicionário = {chave: valor, chave: valor}

Assim como as listas, os dicionários são mutáveis. Mas suas chaves
devem ser de um tipo imutável
Para criar listas usamos colchetes "[]" para criar tuplas usamos
parênteses "()" para criar dicionários usamos chaves "{}"

Exemplo

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

