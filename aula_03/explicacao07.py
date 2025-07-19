
try:
    a = int(input("Diga-me um número: "))
    b = int(input("Diga-me um outro número: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)
except ValueError: #Só executa se esse erro surgir
    print("\nNão podemos converter para um número.")
except ZeroDivisionError: #Só executa se esse erro surgir
    print("\nNão podemos dividir por zero.")
except: #executa para todos os outros erros
    print("\nAlgo muito errado aconteceu!")
finally:
    print("\nO try e except foram finalizados!")