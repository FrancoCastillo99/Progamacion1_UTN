print("Los números pares comprendidos entre 1 y 20 son: ")
for i in range(1,21):
    if i % 2 == 1:
        continue
    else:
        print(i)