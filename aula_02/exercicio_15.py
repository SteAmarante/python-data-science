# Remover um livro pelo título (usando comandos simples).
# Imprimir novamente a biblioteca atualizada.

livro1 = {"Título": "Redes de Computadores 6ª edição",
          "Autor": "Tanenbaum, Andrew S.",
          "Ano": 2021}

livro2 = {"Título": "Arquitetura de Sistemas Operacionais",
          "Autor": "Francis B. Machado, Luiz Paulo Maia",
          "Ano": 2017}

livro3 = {"Título": "Projeto de Banco de Dados: Volume 4" ,
          "Autor": "Carlos Alberto Heuser",
          "Ano": 2009}

lista_dicio = [livro1, livro2, livro3]

while True:
    remover = input("Informe o título do livro que deseja remover: ")
    if remover == livro1["Título"]:
        lista_dicio.remove(livro1)
        break
    elif remover == livro2["Título"]:
        lista_dicio.remove(livro2)
        break
    elif remover == livro3["Título"]:
        lista_dicio.remove(livro3)
        print(lista_dicio)
        break
    else:
        print(f"Livro não encontrado.")