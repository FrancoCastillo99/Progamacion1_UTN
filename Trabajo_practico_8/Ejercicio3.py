import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

num = int(input("Ingrese un número entero: "))

if funciones.par(num):
    print(f"{num} es PAR")
else: 
    print(f"{num} es IMPAR")
               