def sum_price(ticket):
    # Función para calcular la suma de los precios en el ticket
    sum = 0
    for dish, price in ticket:
        sum += price
    return sum

menu = [
    ["Milanesa a la napolitana con papas fritas", 350],
    ["Bife de chorizo a la parrilla con ensalada", 450],
    ["Ravioles de ricota y espinaca con salsa de tomate", 320],
    ["Pechuga de pollo rellena de jamon y queso con pure de papas", 380],
    ["Lomo de cerdo glaseado con miel y vegetales asados", 420]
]

ticket = [] # Lista para almacenar los platos seleccionados en el ticket
recharge = 0 # Variable para almacenar el recargo del método de pago
pay_method = "" # Variable para almacenar el método de pago seleccionado

while True:
    #Opciones
    print("---------------------------------")
    print("1-Mostrar Menu")
    print("2-Agregar plato a ticket")
    print("3-Quitar plato de ticket")
    print("4-Elegir metodo de pago (C-TD-TC)")
    print("5-Mostrar ticket")
    choice = int(input("Ingrese una opción del menu: ")) # Ingreso y guardo la eleccion deseada
    print()
    if choice == 1:
        # Opcion 1
        print("Menú:")
        print()
        print("{:<60} {:>13}".format("Plato", "Precio")) # Muestro nombre de columna y reservo espacios para que quede prolijo
        for index, item in enumerate(menu, start=1):
            dish, price = item #Desempaqueto cada lista
            print(index,"- {:<60} ${:>10.2f}".format(dish, price))
    elif choice == 2:
        # Opcion 2
        while True:
            #Compruebo que el valor elegido sea uno posible
            add = int(input("Elija un plato para agregar: "))-1
            if add>=0 and add<len(menu):
                break
        for i in range(0,len(menu)):
            #Agrego el elemento elegido a la lista ticket
            if i==add:
                ticket.append(menu[add])
        print()
        #Imprimo ticket actual
        print("Ticket actual:")
        print()
        print("{:<60} {:>13}".format("Plato", "Precio"))
        for index, item in enumerate(ticket, start=1):
            dish, price = item
            print(index,"- {:<60} ${:>10.2f}".format(dish, price))
    elif choice == 3:
        #Opcion 3
        if len(ticket) == 0:
            #Verifico que la lista no este vacia, si lo esta reinicio el bucle
            print("El ticket esta vacio, primero agregue un plato para poder quitarlo")
            continue
        while True:
            #Verifico que la eleccion para quitar un plato sea valida
            remove = int(input("Elija un plato para quitar: "))-1
            if remove>=0 and remove<len(ticket):
                break
        for i in range(0,len(ticket)):
            #Remuevo la opcion elegida
            if i==remove:
                ticket.pop(remove)
        print()
        #Imprimo el ticket actual
        print("Ticket actual:")
        print()
        print("{:<60} {:>13}".format("Plato", "Precio"))
        for index, item in enumerate(ticket, start=1):
            dish, price = item
            print(index,"- {:<60} ${:>10.2f}".format(dish, price))
    elif choice == 4 :
        #Opcion 4
        while True:
            #Ingreso metodo de pago, y verifico que sea una de las opciones posibles
            pay_method = input("Ingrese su metodo de pago (C-TD-TC): ").upper()
            if pay_method == "C" or pay_method == "TD" or pay_method == "TC":
                break
        #Defino el recargo segun el metodod el metodo de pago
        if pay_method == "C":
            recharge = 0
        elif pay_method =="TD":
            recharge = 0.05
        elif pay_method == "TC":
            recharge = 0.1
        print(f"El recargo de su metodo de pago es %{int(recharge*100)}")
    elif choice == 5:
        #Opcion 5
        if len(pay_method) == 0:
            #Verifico que el metodo de pago haya sido elegido, si la longitud de la cadena es 0, reinicio el bucle
            print("Elija un metodo de pago primero")
            continue
        if len(ticket) == 0:
            #Verifico la lista ticket no este vacia, si la longitud de la lista es 0, reinicio el bucle
            print("El ticket esta vacio, agregue platos primero")
            continue
        #Muestro el ticket final
        print("------------------------------------------------------------------------------")
        print("Ticket actual:")
        print()
        print("{:<60} {:>13}".format("Plato", "Precio"))
        for index, item in enumerate(ticket, start=1):
            dish, price = item
            print(index,"- {:<60} ${:>10.2f}".format(dish, price))
        print("------------------------------------------------------------------------------")
        print("{:<64} ${:>7}".format("Subtotal: ", sum_price(ticket))) #Muestro el subtotal que es la suma de los precios de los platos
        print("{:<64} ${:>9}".format("Total: ", sum_price(ticket)+(sum_price(ticket)*recharge))) #Muestro el total que es el subtotal mas el recargo correspondiente
        print("------------------------------------------------------------------------------")
        break
    else:
        print("No es una opción valida, vuelva a intentarlo")