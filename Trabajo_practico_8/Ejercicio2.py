import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

n = int(input("Ingrese un número entero: "))
b = int(input("Ingrese un número entero: "))

print()

if funciones.is_pow(n,b):
    print(f"{n} es potencia {b}")
else:
    print(f"{n} NO es potencia {b}")
