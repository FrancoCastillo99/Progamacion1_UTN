# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

days = int(input("¿Cuantos dias va a ingresar?: "))
print()

for i in range(days):
    max_temperature = float(input(f"Ingrese la temperatura maxima del {i+1}° día: "))
    min_temperature = float(input(f"Ingrese la temperatura minimo del {i+1}° día: "))

    print(f"La temperatura promedio del {i+1}° día es {funciones.average_temperature(max_temperature,min_temperature)}")
    print()

