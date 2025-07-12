# verificando a existencia de um item na lista

letras = ["Santo André", "São Bernardo do Campo", "São Caetano do Sul", "Diadema", "Mauá", "Ribeirão Pires", "Rio Grande da Serra"]
var = input("informe uma letra: ")
if var.lower() in letras:
    print(f"A Letra '{var.lower()}' esta na lista")
else:
    print(f"A Letra '{var. lower()}' NÃO esta na lista")