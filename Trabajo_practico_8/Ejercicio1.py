import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

num = int(input("Ingrese un número: "))

print()
print(f"'{num}' tiene {funciones.count_digit(num)} digitos")