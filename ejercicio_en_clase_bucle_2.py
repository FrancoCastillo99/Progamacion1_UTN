num_list= [] #lista que va a contener los numeros ingresados
par = 0 #contador de numeros par
impar = 0 #contador de numeros impar
total_par = 0 #contador de numero par totales
total_impar = 0 #contador de numeros impar totales

#bucle para ingresar numeros, cuando pido 0 corta
while True:
    num = int(input("Ingrese un número (0 cuando desea terminar el ingreso): "))
    if num != 0:
        num_list.append(num)
    else:
        break


for n in num_list: #bucle que recorre los elementos de la lista num_list
    n = str(n) #convierto el numero el string para poder recorrerlo
    for i in n:
        i = int(i) #convierto el string en int para poder realizar calculos matematicos
        if i % 2 == 0: #pregunto si es par, y lo sumo en el contador, caso contrario lo hago en contador de impares
            par += 1
        else:
            impar += 1
    new_par = par #guardo el valor en otra variable para poder vaciar el contador
    new_impar = impar #guardo el valor en otra variable para poder vaciar el contador
    total_par += par #Sumo el total de digitos par 
    total_impar += impar #Sumo el total de digitos impar
    par = 0 #Vacio el contador de par
    impar = 0 #Vacio el contador de impar
    print(f"El número {n}, tiene {new_par} digitos par, y {new_impar} digitos impares") #Muestro cada número y su cantidad de números par e impar
print(f"El total de digitos pares es {total_par}, y el total de impares es {total_impar}") #Muestro total de digitos par e impar