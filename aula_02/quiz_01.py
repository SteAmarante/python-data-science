# Objetivo:
# Os grupos criarão um pequeno Quiz interativo usando condicionais
# e loops no Python.
# Cada grupo deve elaborar 3 perguntas (sobre assuntos diversos ou
# do próprio curso até o momento).
# Utilizar input() para receber respostas e estruturas condicionais
# para validar as respostas dos usuários.
# Usar loops para dar novas chances em caso de erro (máximo de 3
# tentativas por pergunta).

res1 = "Porto Alegre"
res2 = "Nordeste da Africa"
res3 = "Azul e branco"
res4 = "Vermelho e verde"
res5 = "Annelida"
res6 = "1789"

x = 0
while x < 3:
    per1 = str(input("1 - (Melyssa) Qual a capital do Rio Grande do Sul? R: "))
    if per1 == res1:
        break
    else:
        x = x + 1
        print("Resposta incorreta, tente de novo!")

if x < 3:
    x = 0
    while x < 3:
        per2 = str(input("2 - (Phillipe) Aonde fica o Egito? R: "))
        if per2 == res2:
            break
        else:
            x = x + 1
            print("Resposta incorreta, tente de novo!")

    if x < 3:
        x = 0
        while x < 3:
            per3 = str(input("3 - (Stephanie) Quais as cores da bandeira da Finlândia? R: "))
            if per3 == res3:
                break
            else:
                x = x + 1
                print("Resposta incorreta, tente de novo!")

        if x < 3:
            x = 0
            while x < 3:
                per4 = str(input("4 - (Phillipe) Quais cores o daltônico enxerga? R: "))
                if per4 == res4:
                    break
                else:
                    x = x + 1
                    print("Resposta incorreta, tente de novo!")

            if x < 3:
                x = 0
                while x < 3:
                    per5 = str(input("5 - (Stephanie) As minhocas pertencem a qual filo no reino animal na biologia? R:"))
                    if per5 == res5:
                        break
                    else:
                        x = x + 1
                        print("Resposta incorreta, tente de novo!")

                if x < 3:
                    x = 0
                    while x < 3:
                        per6 = str(input("6 - (Melyssa) Quando começa o período contemporâneo? R: "))
                        if per6 == res6:
                            print("Parabéns, você respondeu todas as perguntas!")
                            break
                        else:
                            x = x + 1
                            print("Resposta incorreta, tente de novo!")