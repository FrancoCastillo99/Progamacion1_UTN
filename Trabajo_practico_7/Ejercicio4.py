import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones


list_phrase = []
list_len = []

while True:
    # Ingreso palabras hasta que se ingrese Fin, en ese caso se rompe el bucle
    phrase = input("Ingrese una cadena (Fin para salir): ").capitalize()
    if phrase != "Fin":
        list_phrase.append(phrase)
    else:
        break

for w in list_phrase:
    l = len(w)
    list_len.append(l)

print()
print("La lista ordenada por cantidad de caracteres es: ")
sort_list = funciones.len_sort(list_len,list_phrase)
print()

for i in range(len(list_len)):
    print(f"{sort_list[i]} con {len(sort_list[i])} caracteres")
 

