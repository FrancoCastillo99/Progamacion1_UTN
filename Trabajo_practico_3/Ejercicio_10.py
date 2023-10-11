num = int(input("Ingrese un número: "))
count = 0
if num % 2 == 0:
    half = num // 2
else:
    half = (num - 1) // 2

for i in range(1,half+1):
    if num % i == 0:
        count = count + 1

if count>1:
    print(f"{num} no es primo")
else:
    print(f"{num} es primo")