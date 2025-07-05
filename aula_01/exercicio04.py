#Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o menor ou se são iguais.

nun1 = float(input(" Digite um número: "))
nun2 = float(input(" Digite outro número: "))

if nun1 > nun2:
    print(f"O maior numero é {nun1}")
elif nun1 < nun2:
    print(f"O maior numero é {nun2}")
else:
    print(f"São iguais!")
