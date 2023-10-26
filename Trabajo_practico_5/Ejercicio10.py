# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franc/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

# key= precio, value= descuento
dict_price = {
    400 : 0.15,
    1300 : 0.2,
    150 : 0.1,
    2500 : 0.25
}

# Muestro el diccionario
for key in dict_price:
    value = dict_price[key]
    print(str(key).ljust(6),": ", "%",str(int(value*100)).ljust(6))
print()

print("La lista con los precios nuevos es: ")

new_list_price = funciones.discount(dict_price)

for n in new_list_price:
    print("$",n)