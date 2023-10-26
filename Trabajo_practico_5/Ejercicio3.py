# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

exit_option = False

while exit_option == False:
    dni = input("Ingrese su DNI (sin puntos): ")
    exit_option = funciones.valid_dni(dni)
    if dni.isdigit():
        if exit_option == False:
            print()
            print("DNI invalido, el número debe contener entre 7 y 8 digitos")
    else:
        print()
        print("Debe ingresar solo números, sin letras ni caracteres especiales")
        exit_option = False

name = input("Ingrese su nombre completo: ")
first_name = funciones.get_first_word(name)
last_name = len(funciones.get_last_word(name))


id = first_name + str(last_name)+dni[0:3]

print()
print(f"ID: {id}")