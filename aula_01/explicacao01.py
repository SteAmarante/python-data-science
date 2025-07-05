#O else é executado quando a condição se torna falsa

x=0
while x<5:
    print(x)
    x= x+1
else:
    print("Acabou!")



#Usando o break

x=0
while x<5:
    print(x)
    x= x+1
    if x==3:
        break
else:
    print("Acabou!")