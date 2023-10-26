# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

text = input("Ingrese una cadena: ")
print()

word_and_len = funciones.dict_word(text)

for key in word_and_len:
    value = word_and_len[key]
    print(f"La cadena '{key}', tiene {value} caracteres")