#Ejercicio 1
numero1 = 24
#Ejercicio 2
numero2 = 2.4

#Ejercicio 3 y 4
suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2
division = numero1 / numero2

print("La suma es ",suma)
print("La resta es ",resta)
print("La producto es ",round(producto,2))
print("La division es ",division)

#EJercicio 5
nombre = "Franco"
#Ejercicio 6
precio = 250.49
#Ejercicio 7
descuento = 0.15
#Ejercicio 8
precio_final= round(precio * (1-descuento), 2)

print(f"Mi nombre es {nombre}, y hoy compre un alfajor por {precio}, como mi tarjeta tiene descuento del {descuento*100}% en ese local termine pagando {precio_final}")

#Ejercicio 9
cadena = "Buenos dias"
#Ejercicio 10
longitud = len(cadena)

print(f"La frase \"{cadena}\" tiene una longitus de {longitud} carateres")

#Ejercicio 11
precio = int(540.50)
print(f"El precio convertido a entero es {precio}")

#Ejercicio 12
nombre = "Franco"
apellido = "Castillo"
nombre_apellido = nombre + " " + apellido
print(f"Mi nombre completo es {nombre_apellido}")

#Ejercicio 13
edad = 24
edad = edad + 5 -10
print(f"Mi edad modificada es {edad}")

#Ejercicio 14
altura = 1.74
altura = 1.74 * 4 / 3
print(f"MI altura modificada es {altura}")

#Ejercicio 15
nombre_mayuscula = "FRANCO JESÚS CASTILLO"
nombre_minuscula = nombre_mayuscula.lower()

print(f"Mi nombre en minuscula es  {nombre_minuscula}")

#Ejercicio 16
nombre_primera_mayuscula = nombre_minuscula.capitalize()

print(f"Mi nombre escrito con la primer letra en mayucula es {nombre_primera_mayuscula}")
