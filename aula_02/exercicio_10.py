# Crie uma tupla números = (5, 10, 15, 20) e converta-a em uma lista.
# Adicione o número 25 à lista resultante depois volte a lista para tupla e print ela.

numeros = (5, 10, 15, 20)
lista_numeros = list(numeros)
lista_numeros.append(25)
nova_numeros = tuple(lista_numeros)
print(nova_numeros)