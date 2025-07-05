#Crie um programa que solicite ao usuário uma nota entre zero e dez. 
# Se o valor informado for inválido, exiba uma mensagem de erro e continue solicitando 
# uma nota válida até que o usuário a forneça.

nota = int(input("Digite uma nota: "))

while nota > 10 or nota < 0:
    print(f"Nota invalida tente de novo!")
    nota = int(input("Digite uma nota: "))
else:
    print(f"Nota válida!")