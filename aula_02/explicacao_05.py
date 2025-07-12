#Adicionando elementos fornecidos pelo usuário à lista

nova = []
while True:
    num = int(input("Digite um numero inteiro(0 para sair): "))
    if num == 0:
        break
    nova. append(num)
nova.sort() #Para ordenar os itens de uma lista usamos o método sort
print(nova)