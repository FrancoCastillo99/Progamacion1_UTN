num = int(input("Ingrese un número: "))
for i in range(num,-1,-1):
    if i>0:
        print(i,end = ",")
    else:
        print(i)