# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

number = input("Ingrese un número: ")
digit = input("Ingres el digito que desea buscar: ")

matches = funciones.find_digit(number,digit)

print()

if matches == 0:
    print(f"El digito '{digit}', no se encuentra en {number}")
else:
    print(f"El digito '{digit}', se encontro {matches} vez/veces en {number}")