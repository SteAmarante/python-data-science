## Crie uma função chamada par_ou_impar que receba um nuúmero como parametro e retorne "par" se ele for par e "impar" se ele for impar.
##

def par_ou_impar(nun1):
    """
    Função que recebe um numero e retorne "par" se ele for par e "impar" se ele for impar.
    """
    if nun1 != 0:
        if nun1  % 2 == 0:
            print(f"É par!")
        elif nun1 % 2 != 0:
            print(f"É impar!")
    else:
        print(f"É zero!")

nun1 = int(input("Digite um número inteiro: "))
print(par_ou_impar(nun1))