# Crie uma função cubica(*nums) que devolve uma lista com o cubo de cada número
# recebido. Use for.


def cubica(*nums):
    """
    Função que retorna uma lista de cubo dos numeros informados.
    """
    cubos = [] 
    for i in nums:
       x = (i**3)
       cubos.append(x)
       print(cubos)

cubica(2, 3, 6, 8, 9, 11)