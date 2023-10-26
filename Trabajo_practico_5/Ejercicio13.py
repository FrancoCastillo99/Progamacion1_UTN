# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

while True:
    dimension = int(input("¿Cual es la dimension del vector?: "))
    if dimension >= 1 and dimension <=3:
        break
    else:
        print("Debe ingresar un número entre 1 y 3 (comprendidos)")

if dimension == 1:
    x = int(input("Ingrese la componente en x del vector: "))
    mod = funciones.vect_module(x)
elif dimension == 2:
    x = int(input("Ingrese la componente en x del vector: "))
    y = int(input("Ingrese la componente en y del vector: "))
    mod = funciones.vect_module(x,y)
elif dimension == 3:
    x = int(input("Ingrese la componente en x del vector: "))
    y = int(input("Ingrese la componente en y del vector: "))
    z = int(input("Ingrese la componente en z del vector: "))
    mod = funciones.vect_module(x,y,z)

print()
print(f"El modulo del vector es {mod}")

