# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

radius = float(input("Ingrese el radio del circulo: "))

# Desempaqueto la lista que devuelve la funcion
area, circum = funciones.area_circum(radius)

print()
print(f"El area del circulo de radio {radius}, es {round(area, 2)}")
print(f"La circunferencia del circulo de radio {radius}, es {round(circum, 2)}")