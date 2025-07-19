# Crie uma função contar_pares(*n) que conte e retorne quantos números pares
# existem nos parametros passados.

def contar_pares(*n):
    """
    Função conta quantidade de pares informados
    """
    contador = 0
    for i in n:
        if i % 2 == 0:
            contador += 1
    return contador

qtd_pares = contar_pares(2, 8, 4, 60, 5, 11, 3, 33, 26) 
print(qtd_pares)   
