x = 0
while x<=30:
    x = x + 1
    if x == 4 or x == 6 or x == 10:
        print(f"Se salto el valor {x} de x")
    elif x ==15:
        print(f"Se rompio la ejecución del bloque cuando x valía: {x}")
        break;
    else:
        print(x)
