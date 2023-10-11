first_year = int(input("Ingrese el primer año: "))
second_year = int(input("Ingrese el segundo año: "))

print("---------------------------------------------------")

for i in range(first_year,second_year+1):
    if (i % 4 == 0 and i % 100 != 0) or i % 10 == 0:
        print(i)
