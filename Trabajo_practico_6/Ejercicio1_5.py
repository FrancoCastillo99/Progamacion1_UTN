import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

list_num = []

while True:
    # Ingreso numeros hasta que se ingrese un 0, en ese caso se rompe el bucle
    num = int(input("Ingrese un número (0 para salir): "))
    if num != 0:
        list_num.append(num)
    else:
        break

print()
remove = int(input("Ingrese el número que desea borrar: "))

list_num = funciones.remove_number(list_num, remove)

print()
print("La sumatoria de los elementos de la lista es: ")
print(funciones.summation(list_num))

print()
limit = int(input("Ingrese un número a partir del cual se creara una nueva lista con solo números menores a el: "))

print()
print("La nueva lista es: ")
list_less = funciones.numbers_less(list_num, limit)

for n in list_less:
    print(n, end = " ")

print()
print("A continuación se mostrara cada elemento de la lista original y cuantas veces esta repetido: ")
print()
repeat_list = funciones.repeated_numbers(list_num)

for t in repeat_list:
    num, repeat = t
    print(f"Número: {num}, Repeticiones: {repeat}")