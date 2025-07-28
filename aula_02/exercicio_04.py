# Numa eleição existem três candidatos: Faça um programa que peça o número total de eleitores.
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

# Contador de votos para cada candidato
can1 = 0
can2 = 0
can3 = 0

# Pedir o número total de eleitores
total_eleitores = int(input("Digite o número total de eleitores: "))

# Coletar os votos de cada eleitor
for i in range(total_eleitores):
    print(f"\nEleitor {i+1}:")
    voto = input("Digite o número do candidato (1, 2 ou 3): ")
    
    # Contabilizar o voto
    if voto == '1':
        can1 += 1
    elif voto == '2':
        can2 += 1
    elif voto == '3':
        can3 += 1
    else:
        print("Voto inválido! (Digite 1, 2 ou 3)")

# Mostrar os resultados
print("\nResultado da eleição:")
print(f"Candidato 1: {can1} votos")
print(f"Candidato 2: {can2} votos")
print(f"Candidato 3: {can3} votos")
