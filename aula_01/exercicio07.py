# Calcule a obrigatoriedade do voto para uma pessoa dependendo de sua idade. 
#(16, 18 e 70)
#voto é facultativo:
#maiores de 16 anos e menores de 18 anos;
#maiores ou igual a 70 anos.

voto = int(input("Coloque a sua idade para saber se você tem que votar: "))

if voto < 16:
    print(f"Volta pra casa!")
elif (voto >= 16 and voto < 18) or voto >= 70:
    print(f"Voto é facultativo!")
else:
    print(f"Voto é obrigatório!")

