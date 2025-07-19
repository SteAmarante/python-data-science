## Crie uma função chamada apresentação que receba um nome, idade, e um curso como parametro e imprima uma mensagem de apresetnação para a sala, sendo que o curso terá como valor padrão "Curso FIC SENAI"
##

def apresentacao(nome, idade, curso="FIC SENAI"):
    """
    Essa função apresentará a pessoa passada por parâmetro
    """
    print(f"Olá eu sou {nome} tenho {idade} e estou no curso {curso}")

apresentacao("Stephanie", 28, "Python para Data Science")
