# Parcial de Franco Castillo, DNI: 41699948

even = [] #lista para guardar numeros par
odd = [] #lista para guardar numeros impares
name = input("Ingrese su nombre: ").capitalize() #Ingreso un nombre y capitalize para poner la primer letra mayuscula y las demas minuscula

while True:
    # Menu de opciones
    print("-----------------------------------------")
    print(f"{name} elija a que desea jugar (Usando los números): ")
    print("1-Juego de números")
    print("2-Juego de palabras")
    choice = int(input())

    if choice == 1:
        #Opcion 1
        while True:
            num = int(input("Ingrese un número (0 para salir): "))
            if num == 0:
                #Si ingreso un 0, termino de ingresar números
                break
            if num % 2 == 0:
                # Si es par, lo agrego a even
                even.append(num)
            else:
                # Si es impar lo agrego a odd
                odd.append(num)

        larger = 0; #Variable para almacenar el mayor valor
        for n in even:
            if n > larger:
                # Si n es mayor a larger, lo guardo en larger
                larger = n
        print(f"{name}, el mayor número par ingresado es {larger}")

        sum = 0 # Variable para ir sumando los numeros impares
        for n in odd:
            sum += n
        average = round(sum / len(odd),2) # Calculo el promedio, y lo redondeo a dos cifras significativas
        print(f"{name}, el promedio de los números impares es {average}")

        break # Salgo del bucle

    if choice == 2:
        # Opcion 2
        phrase = input(f"{name}, ingrese una frase: ")

        #Contadores para cada vocal
        count_a = 0
        count_e = 0
        count_i = 0
        count_o = 0
        count_u = 0


        for l in phrase:
            # Recorro la cadena, y voy comparando cada caracter con las vocales, si coincide aumento en 1 el contador correspondiente 
            if l == "a":
                count_a += 1
            if l == "e":
                count_e += 1
            if l == "i":
                count_i += 1
            if l == "o":
                count_o += 1
            if l == "u":
                count_u += 1
        
        print(f"{name}, la frase ingresada '{phrase}', tiene: ")
        print(f"Cantidad de letra 'a': {count_a}")
        print(f"Cantidad de letra 'e': {count_e}")
        print(f"Cantidad de letra 'i': {count_i}")
        print(f"Cantidad de letra 'o': {count_o}")
        print(f"Cantidad de letra 'u': {count_u}")

        break # Salgo del buble