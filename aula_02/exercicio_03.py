# Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a
# quantidade de pessoas por geração:
# Baby Boomers: 60 a 78 anos (em 2024).
# Geração X: 44 a 59 anos (em 2024).
# Millennials (Geração Y): 28 a 43 anos (em 2024).
# Geração Z: 14 a 27 anos (em 2024).
# Geração Alpha: Até 14 anos (em 2024)

baby = 0
gx = 0
mille = 0
genz = 0
alpha = 0
qtde = int(input("Digite a quantidade de pessoas para responder: "))

for i in range(qtde):
    idade = int(input("Digite a idade: "))

    if idade >= 60 and idade <= 78:
        baby = baby + 1
    elif idade >= 44 and idade <= 59:
        gx = gx + 1
    elif idade >= 28 and idade <= 43:
        mille = mille + 1
    elif idade >= 15 and idade <= 27:
        genz = genz + 1
    elif idade <= 14:
        alpha = alpha + 1
    
print(f"Há {baby} da geração Baby Boomers: 60 a 78 anos (em 2024), {gx} da Geração X: 44 a 59 anos (em 2024), {mille} de Millennials (Geração Y): 28 a 43 anos (em 2024), {genz} da Geração Z: 14 a 27 anos (em 2024) e {alpha} da Geração Alpha: Até 14 anos (em 2024)")
