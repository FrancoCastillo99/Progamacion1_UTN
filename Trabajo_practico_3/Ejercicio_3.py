num = int(input("Ingrese un número: "))
print(f"Numeros impares entre 1 y {num}")
for i in range(1,num+1):
    if i%2==1:
        print(i)