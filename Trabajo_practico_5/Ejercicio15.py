# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

list_num = []
list_factorial = []

while True:
    # Ingreso numeros hasta que se ingrese un 0, en ese caso se rompe el bucle
    num = int(input("Ingrese un número (0 para salir): "))
    if num != 0:
        list_num.append(num)
        # Agrego a la lista de factoriales lo que me devuelve la funcion 
        list_factorial.append(funciones.factorial(num))
    else:
        break

print()
for i in range(len(list_num)):
    print(f"El factorial de {list_num[i]}, es {list_factorial[i]}")



