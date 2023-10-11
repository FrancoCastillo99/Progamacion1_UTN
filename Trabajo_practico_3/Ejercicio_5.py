cash = float(input("Ingrese el dinero a invertir: "))
an_interest = float(input("Ingrese el interes anual: "))
years = int(input("Ingrese cuantos años dejara el dinero: "))

for i in range(years):
    cash = cash + (cash * (an_interest/100))
    print(f"Dinero actual luego de {i} año/s: {cash}")