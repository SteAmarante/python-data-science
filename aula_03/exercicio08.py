# Crie uma função de divisão segura, que evite divisão por zero usando try e except.
# Além disso use o finally para informar que a operação foi realizada.

def divisao_segura(a,b):
    """
    Função de divisão segura, que evite divisão por zero usando try e except.
    """
    try:
        print(f"A divisão é: {a/b}")
    except ZeroDivisionError: #Só executa se esse erro surgir
        print("\nNão podemos dividir por zero.")
    finally:
        print("\nO try e except foram finalizados!")


a = int(input("Diga-me um número: "))
b = int(input("Diga-me um outro número: "))
divisao_segura(a,b)