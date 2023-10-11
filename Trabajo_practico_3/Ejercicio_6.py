num_stars = int(input("Ingrese un número para construir el triangulo: "))
for i in range(1,num_stars+1):
    for j in range(i):
        print("*",end= "")
    print()