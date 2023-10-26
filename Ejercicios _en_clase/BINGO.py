import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

import random

while True:
    # Creo la lista donde guardaremos las filas de números
    bingo_card = []

    while True:
        # Creo la lista donde ingresaremos los números
        rows = []
        while True:
            element = int(input("Ingrese un número para llenar el carton (sin repetir, y comprendido entre 1 y 75): "))
            if element in rows:
                # Si el número ingresado ya esta en la lista, no lo agrego y vuelvo a pedir otro
                print(f"El número {element}, ya se encuentra en el carton, ingrese uno distinto")
                continue
            elif element<1 or element>75:
                # Si el número ingresado es menor a 1 o mayor a 75 no lo agrego y pido otro
                print("Debe ingresar un número comprendido entre 1 y 75")
            else: 
                # Si cumple las condiciones deseadas, agrego element a la lista row
                rows.append(element)
                if len(rows)==5:
                    # Si la lista row tiene 5 elemento salgo del bucle
                    break
        
        # Agrego la lista rows a la lista bingo_card
        bingo_card.append(rows)

        if len(bingo_card) == 5:
            # Si la lista bingo_card contiene 5 listas salgo del bucle
            break
        else:
            # Si tiene menos de 5 listas, pido otra
            print("Ingrese la siguiente fila")
            print()

    print("Carton BINGO!")
    print()

    # Muestro el carton 
    funciones.show_list(bingo_card)

    print()

    # Declaro una variable para contar los intentos hasta lograr el bingo
    attempts = 1

    # Creo una variable para verificar si se logro el bingo
    bingo_finish = False


    while True:
        print(f"{attempts}° intento!")
        print()

        # Obtengo un número random entre 1 y 75
        check_element = random.randint(1,75)

        print()

        for i in range(len(rows)):
            for j in range(len(rows)):
                # Recorro la lista bingo_card
                if check_element == bingo_card[i][j]:
                    # Si el númeor random coincide con algun elemento de la lista, asigno X a dicha posición
                    bingo_card[i][j] = "X"
        
        # Armo una lista  pero que contiene las columnas agrupadas en listas en lugar de las filas
        columns = [list(column) for column in zip(*bingo_card)]

        # Armo una lista con los elementos de la diagonal principal
        main_diagonal = [bingo_card[i][i] for i in range(len(bingo_card))]

        # Armo una lista con los elementos de la digonal secundaria
        secondary_diagonal = [bingo_card[i][-(i+1)] for i in range(len(bingo_card))]


            
        print("Carton BINGO!")
        print()

        #Muestro la lista actual con los aciertos
        funciones.show_list(bingo_card)


        for r in bingo_card:
            if funciones.bingo(r):
                # Si una fila esta completa de X, tenemos BINGO
                print("BINGO en fila!!!")
                print()
                bingo_finish = True
                break
        
        for c in columns:
            if funciones.bingo(c):
                # Si una columna esta completa de X, tenemos BINGO
                print("BINGO en columna!!!")
                print()
                bingo_finish = True
                break
        
        if funciones.bingo(main_diagonal):
            # Si la diaognal principal esta completa de X, tenemos BINGO
            print("BINGO en Diagonal Principal!!!")
            print()
            bingo_finish = True
            break

        if funciones.bingo(secondary_diagonal):
            # Si la diaognal secundaria esta completa de X, tenemos BINGO
            print("BINGO en Diagonal Inversa!!!")
            print()
            bingo_finish = True
            break

        attempts += 1  

        if bingo_finish:
            break  

        # Pido interacción para que se tire la proxima bola
        other_attempt = input("Proximo bola? s/n: ").lower()
        print()

        if other_attempt == "n":
            # Si elige n, sale del juego aun sin ganar
            break

    print()
    # Pregunto si quiere volver a jugar
    other_game = input("¿Quiere vovler a jugar? s/n: ").lower()
    print()
    
    if other_game == "n":
        # Si elige n salgo, caso contrario se reinicia el juego
        break
    

