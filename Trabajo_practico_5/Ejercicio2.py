# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

phrase = input("Ingrese una frase: ")

print(f"La palabra final es '{funciones.get_last_word(phrase)}'")