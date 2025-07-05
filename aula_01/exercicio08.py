#Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias:
#Infantil A = 5 a 7 anos 
#Infantil B = 8 a 11 anos
#Juvenil A = 12 a 13 anos
#Juvenil B = 14 a 17 anos
#Adultos = Maiores de 18 anos

idade_nadador = int(input("Digite a idade para saber qual categoria você se enquadra: "))

if idade_nadador < 4:
    print(f"Não tem idade para fazer as aulas!")
elif idade_nadador >= 5 and idade_nadador <= 7:
    print(f"Categoria: Infantil A.")
elif idade_nadador >= 8 and idade_nadador <= 11:
    print(f"Categoria: Infantil B.")
elif idade_nadador >= 12 and idade_nadador <= 13:
    print(f"Categoria: Juvenil A.")
elif idade_nadador >= 14 and idade_nadador <= 17:
    print(f"Categoria: Juvenil B.")
else:
    print("Adultos.")