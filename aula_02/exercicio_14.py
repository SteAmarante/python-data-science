# Crie uma estrutura contendo uma lista com três dicionários, onde cada dicionário
# represente um livro com título, autor e ano. Em seguida, imprima as informações
# dos livros utilizando loop (for).

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

for i in range(3):
    print(lista_dicio[i])