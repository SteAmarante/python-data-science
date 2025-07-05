#6. Faça um programa que solicite dois números ao usuário (com decimais) 
#Em seguida solicite que o usuário informe a operação matemática (soma, subtração, multiplicação e divisão) 
# e print o resultado da operação escolhida.

nun1 = int(input("Digite um numero:"))
nun2 = int(input("Digite outro numero:"))
op_mat = input("Digite a operação matemática (soma, subtração, multiplicação e divisão) escolhida: ")

if op_mat == "soma":
    print(f"O resultado da soma é {nun1+nun2}")
elif op_mat == "subtração":
    print(f"O resultado da subtração é {nun1-nun2}")
elif op_mat == "multiplicação":
    print(f"O resultado da multiplicação é {nun1*nun2}")
else:
    print(f"O resultado da sua divisão é {nun1/nun2}")
    