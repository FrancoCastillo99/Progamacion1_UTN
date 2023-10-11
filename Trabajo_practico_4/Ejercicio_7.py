while True:
    print("---------------------------------")
    print("1-Opcion A")
    print("2-Opcion B")
    print("3-Opcion C")
    choice = int(input("Ingrese una opción del menu (0 para salir): "))
    print()
    if choice == 1:
        print("Eligio la opción A")
    elif choice == 2:
        print("Eligio la opción B")
    elif choice == 3:
        print("Eligio la opción C")
    elif choice == 0:
        print("Eligio salir")
        break
    else:
        print("No es una opción valida, vuelva a intentarlo")