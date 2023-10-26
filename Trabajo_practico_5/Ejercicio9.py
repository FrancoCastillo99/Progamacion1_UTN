# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

# Variable para sumar los intentos
tries = 0

while True:
    user = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    print()

    # Desempaqueto la lista que devuelve la funcion
    successful, attempt = funciones.login(user, password)

    # Sumo cada intento a la variable 
    tries += attempt

    if successful:
        # Si la funcion devuelve True, muestro el mensaje y salgo
        print(f"El ingreso fue exitoso, {tries} intentos realizados")
        break
    elif tries == 3:
        # Si la funcion devuelve False, y el numero de intentos es igual a 3, muestro mensaje y salgo
        print(f"Ingreso denegado, supero el limite de intentos ({tries})")
        break

