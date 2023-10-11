all_line = []

while True:
    line = input("Ingrese una frase (o espacio para finalizar): ")
    if line == " ":
        break
    else:
        line_cap = line.upper()
        all_line.append(line_cap)

print("-----------------------------------------")
    
for n in all_line:
    print(n)