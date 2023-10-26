# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

list_prime = []

while True:
    # Ingreso numeros hasta que se ingrese un 0, en ese caso se rompe el bucle
    num = int(input("Ingrese un número primo (cuando ingrese un NO primo sale): "))
    if funciones.prime_number(num):
        list_prime.append(num)
    else:
        break
print()

for n in list_prime:
    print("--------------------------------------------------------------------------------")
    print(f"La suma de los digitos de '{n}', da como resultado {funciones.add_digit(n)}")
    print()
    search = input("Ingrese el digito que desea buscar: ")
    
    matches = funciones.find_digit(str(n), search)

    print()

    if matches == 0:
        print(f"El digito '{search}', no se encuentra en {n}")
    else:
        print(f"El digito '{search}', se encontro {matches} vez/veces en {n}")

print()
print(f"El número mas grande de los ingresados es {max(list_prime)}, y su factorial es {funciones.factorial(max(list_prime))}")