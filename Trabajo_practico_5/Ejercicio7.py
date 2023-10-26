# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

list_num = []

while True:
    # Ingreso numeros hasta que se ingrese un 0, en ese caso se rompe el bucle
    num = int(input("Ingrese un número (0 para salir): "))
    if num != 0:
        list_num.append(num)
    else:
        break

# Desempaqueto la lista que devuelve la funcion 
max_num, min_num = funciones.max_min(list_num)

print()
print(f"El número maximo ingresado es: {max_num}")
print(f"El número minimo ingresado es: {min_num}")