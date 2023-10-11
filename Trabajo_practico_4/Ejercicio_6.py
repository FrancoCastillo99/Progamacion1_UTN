num_list = [5,7,6,10,12,14,17,19,20]
salir = False

while True:
    search = int(input("Ingrese el número que desea buscar: "))
    for n in num_list:
        if n == search:
            print(n)
            salir = True
            break
    if salir:
        break
    else:
        print("No se encontro el número, pruebe otro")
        print()

