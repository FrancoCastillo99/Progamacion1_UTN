num_list= []
par = 0
impar = 0
total_par = 0
total_impar = 0

while True:
    num = int(input("Ingrese un número (0 cuando desea terminar el ingreso): "))
    if num != 0:
        num_list.append(num)
    else:
        break

for n in num_list:
    n = str(n)
    for i in n:
        i = int(i)
        if i % 2 == 0:
            par += 1
        else:
            impar += 1
    new_par = par
    new_impar = impar
    total_par += par
    total_impar += impar
    par = 0
    impar = 0
    print(f"El número {n}, tiene {new_par} digitos par, y {new_impar} digitos impares")
print(f"El total de digitos pares es {total_par}, y el total de impares es {total_impar}")