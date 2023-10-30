import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

list_word = []

while True:
    # Ingreso palabras hasta que se ingrese Fin, en ese caso se rompe el bucle
    word = input("Ingrese una palabra (Fin para salir): ").capitalize()
    if word != "Fin":
        list_word.append(word)
    else:
        break

selection_list = funciones.selection_sort(list_word)

print()
print("La lista de nombres ingresados, ordenados de forma ascendente: ")
print()
for w in selection_list:
    print(w)