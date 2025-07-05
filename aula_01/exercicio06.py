#Faça um Programa que verifique o estado civil de uma pessoa. Se a letra digitada é
#"C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros).
#Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil

est_civil = input("Digite a letra do estado civil C (Casado), S (Solteiro), D (Divorciado), V (Viúvo) ou O (outros): ")

if est_civil == "C":
    print("c - casado(a)")

elif est_civil == "S":
    print("s - solteiro(a)")

elif est_civil == "D":
    print("d - divorciado(a)")

elif est_civil == "V":
    print("v - viuvo(a)")

else:
    print("o - outros(as)")