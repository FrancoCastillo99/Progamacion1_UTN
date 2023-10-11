prime_numbers = []

def is_prime(num):
    count = 0
    if num % 2 == 0:
        half = num // 2
    else:
        half = (num - 1) // 2

    for i in range(1,half+1):
        if num % i == 0:
            count = count + 1

    if count>1:
        return False
    else:
        return True

while True:
    while True:
        num = int(input("Ingrese un número mayor a 1 (o 0 para finalizar): "))
        if num == 0 or num > 1:
            break
        elif num <= 1:
            print("Debe ser mayor a 1")
    if num == 0:
        break
    else:
        if is_prime(num):
            prime_numbers.append(num)

print("-----------------------------------------")

print("Los numeros primos son: ")
for n in prime_numbers:
    print(n)