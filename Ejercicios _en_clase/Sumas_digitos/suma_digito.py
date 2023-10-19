# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franco Castillo/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

list_num = [] # Lista donde se van a guardar todos los números ingresados 

while True:
    num = int(input("Ingrese un número: "))
    list_num.append (num) 

    # Muestro el número y la suma de sus digitos usando la funcion add_digit
    print(f"La suma de los digitos de '{num}' es {funciones.add_digit(num)}") 

    # Pregunto si desea ingresar otro número, ingresando s (si) o n (no)
    other_num = input("¿Ingresar otro número? (s/n): ").lower()
    print()

    # Si ingresa algo distinto de s, salgo del bucle
    if other_num != "s":
        break

# Llamo la función summation y le paso la lista con todos los números
summ = funciones.summation(list_num)

# Muestro la sumatoria y la suma de los digitos de la misma
print(f"La suma de todos los números ingresados es {summ}")
print(f"La suma de los digitos de la sumatoria es {funciones.add_digit(summ)}")
