#Escreva um programa em Python que recebe um inteiro e diga se é par ou ímpar ou se está zerado.

nun1 = int(input("Digite um número inteiro: "))

if nun1 != 0:
    if nun1  % 2 == 0:
        print(f"É par!")
    elif nun1 % 2 != 0:
        print(f"É impar!")
else:
    print(f"É zero!")