# Modularização simples
# Divida um pequeno programa que calcula o Índice de Massa Corporal (IMC) em duas
# funções:
# Uma função para entrada dos dados (peso e altura).
# Outra função para cálculo e exibição do IMC.

## Primeira parte -----------------------
# Parte da Função
def imc(peso, altura):
    """
    Função que calcula o IMC a partir de um determinado peso e altura
    """
    imc = peso/ (altura*altura)
    return imc

## Segurada parte -----------------------
# Parte de processamento das informações

peso = float(input("Digite o seu peso (em Kg): "))
altura = float(input("Digite sua altura (em Metros com ponto): "))
if peso != 0 and altura != 0:
    imc_retornado_pro_peso_altura_do_usuario = imc(peso, altura)
    print(f"Seu IMC é {imc_retornado_pro_peso_altura_do_usuario:.2f}")
else:
    print("Peso ou altura zerados. Informe dois valores diferentes de 0 (zero)")