# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

dni = input("Ingrese su DNI (sin puntos): ")

if funciones.valid_dni(dni) == True:
    print("DNI valido")
else:
    print("DNI invalido, el numero debe tener entre 7 y 8 digitos")
