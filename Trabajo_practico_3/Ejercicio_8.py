num = int(input("Ingrese un número para construir el triangulo: "))
for i in range(1,num+1,2):
    while i>=1:
        print(i, end = " ")
        i=i-2
    print()