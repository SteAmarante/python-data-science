# *args significa arguments. Quando você usa args, a função pode aceitar vários valores. O sinal `*` (asterisco) antes do
# nome é o que indica isso *args. Quando você passa *args como um parâmetro, ele é tratado como uma tupla que contém
# todos os argumentos posicionais passados quando você chama a função. Esse recurso é particularmente útil quando você
# não tem certeza sobre o número de argumentos que sua função pode receber.
# OBS:. Você pode usar outro nome invés de args, veja o exemplo:

def calculate_sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

result = calculate_sum(5, 10, 15, 20, 55, 345, 1)
print(result)