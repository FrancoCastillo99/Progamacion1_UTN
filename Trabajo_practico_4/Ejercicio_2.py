bank = 0
print("Ingrese depositos (D xxx), o retiros (R xxx)")
while True:
    trans = input()
    if trans == " ":
        break
    else:
        if trans[0:trans.find(" ")] == "D":
            bank = bank + int(trans[trans.find(" ")+1:len(trans)])
        elif trans[0:trans.find(" ")] == "R":
            bank = bank - int(trans[trans.find(" ")+1:len(trans)])

print("-----------------------------------------")
print(f"Quedan ${bank} en la cuenta")