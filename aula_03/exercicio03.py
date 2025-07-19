##Crie uma funçaõ que converta uma temperatra de fahrenheit para Celcius e para Kelvin e print os dois##

def fahr_to_celsius_to_kelvin(temp):
    """
    Função que recebe como argumento uma temperatura
    em Fahrenheit e converte ela para Celsius e para Kelvin e imprime os dois
    """
    c = (temp-32)*(5/9)
    k = c + 273
    print(f"Sua temperatura {temp} em Celsius será {c:.2f} e em Kelvin será {k:.2f}")

fahr_to_celsius_to_kelvin(float(input("Digite a temperatura em Fahrenheit: ")))
