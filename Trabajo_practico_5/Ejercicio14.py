# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

number = int(input("Ingrese un número: "))

if funciones.prime_number(number):
    print(f"{number} es primo")
else:
    print(f"{number} NO es primo")