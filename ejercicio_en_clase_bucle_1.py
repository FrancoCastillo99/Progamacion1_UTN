import string 

alphabet = list(string.ascii_lowercase) # Importo string y uso el metodo ascii_lowercase para guardar todas las letras del abecedario en una lista

move = int(input("Ingrese la cantidad de lugares que quiere correr cada letra: "))

word_list = [] # Creo la lista que contendra las palabras originales
word_final = "" #Creo la variable donde voy a armar la palabra modificada
word_final_list = [] #Creo la lista donde voy a guardar las palabras modificadas

print("Ingrese el mensaje (las 5 palabras que desea encriptar) : ")

#Ingreso las palabras y las agrago a la lista 
for i in range(5):
    word = list(input().lower())
    word_list.append(word)

#Recorro la lista 
for m in word_list:
    #Recorro la palabra
    for i in range(len(m)):
        char = m[i]
        if char in alphabet: #Pregunto si la letra que saque de la palabra esta contenida en la lista alphabet
            n = (alphabet.index(char)+move) % 26 #Creo el indice de la letra corrida
            word_final += alphabet[n] #Agrego cada letra modificada a la varieble
        else:
            word_final += char #Si el caracter no esta contenido en la lista alphabet guardo el mismo caracter que ya existia
    else:
        word_final_list.append(word_final)   #Agrego la nueva palabra a la nueva lista
        word_final="" #Vacio la variable donde se guardan las palabras modificadas

print(word_final_list) #Muestro la lista con las palabras encriptadas
