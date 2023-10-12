menu = [
    ["Milanesa a la napolitana con papas fritas", 350]
    ["Bife de chorizo a la parrilla con ensalada", 450]
    ["Ravioles de ricota y espinaca con salsa de tomate", 320]
    ["Pechuga de pollo rellena de jamon y queso con pure de papas", 380]
    ["Lomo de cerdo glaseado con miel y vegetales asados", 420]
]

while True:
    print("---------------------------------")
    print("1-Mostrar Menu")
    print("2-Agregar plato a ticket")
    print("3-Quitar plato de ticket")
    print("4-Elegir metodo de pago (C-TD-TC)")
    PRINT("5-Mostrar ticket")
    choice = int(input("Ingrese una opción del menu (0 para salir): "))
    print()
    if choice == 1:
        print(menu)
    elif choice == 2:
        print("Eligio la opción B")
    elif choice == 3:
        print("Eligio la opción C")
    elif choice == 0:
        print("Eligio salir")
        break
    else:
        print("No es una opción valida, vuelva a intentarlo")