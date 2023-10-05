import string 

alphabet = list(string.ascii_lowercase)

move = int(input("Ingrese la cantidad de lugares que quiere correr cada letra: "))

word_list = []
word_final = ""
word_final_list = []

print("Ingrese el mensaje (las 5 palabras que desea encriptar) : ")

for i in range(5):
    word = list(input().lower())
    word_list.append(word)

for m in word_list:
    for i in range(len(m)):
        char = m[i]
        if char in alphabet:
            n = (alphabet.index(char)+move) % 26
            word_final += alphabet[n]
        else:
            word_final += char
    else:
        word_final_list.append(word_final)   
        word_final=""

print(word_final_list)
