# Importo sys para poder acceder a un archivo fuera de la carpeta actual
import sys
sys.path.append('C:/Users/Franco Castillo/Progamacion1_UTN')
# Importo el archivo de funciones
import funciones

# Lista con las palabras a adivinar 
footbal_players = ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappe", "Robert Lewandowski", "Sergio Ramos", "Mohamed Salah", "Virgil van Dijk", "Kevin De Bruyne", "Luka Modric"]

# Llamo a la funcion rand_player que me devuelve un jugador random de la lista 
player = funciones.rand_player(footbal_players)
player = player.lower()
# Reemplazo todas las letras de la palabra por "-"
clone_player = ''.join(['-' if c.isalpha() else c for c in player])

print("Vamos a jugar a adivinar el jugador de Futbol!")
print("Empieza el juego!")
print()
# Establezco el contador de vidas en 6
lives_counter = 6

while True:
    # Muestro la palabra a adivinar en su estado actual
    print(clone_player)

    while True:
        letter = input("Intente adivinar una letra!: ")

        # Verifico si ingreso una sola letra
        if len(letter) > 1:
            print("Ingrese una sola letra!")
        else:
            break

    # Convierto la palabra oculta en una lista
    clone_player_list = list(clone_player)  

    if letter in player:
        for i in range(len(player)):
            if player[i] == letter:
                # Cuando encuentre una coincidencia entre la letra ingresada y una presente en la palabra reemplazo el "-" por la letra en cuestion
                clone_player_list[i] = letter
        clone_player = ''.join(clone_player_list)
        print("¡Bien! Acertó una letra.")
        print()
        lives_counter = 6 # Reestablezco el contador de vidas
    else:
        lives_counter -= 1 # Si no se cuentra la coindcidencia, el contador baja en 1 unidad
        print(f"{letter} no se encuentra en la palabra, le quedan {lives_counter} vidas ")  
        print()
      
    if lives_counter == 0 :
        # Si el contador llega a 0, muestro mensaje y salgo
        print(f"Se quedo sin vidas, la palabra era '{player.title()}'")
        break
    elif clone_player == player:
        # Si la palabra que fuimos adivinando coincide con la seleccion original, muestro mensaje y salgo
        print(player.title())
        print("Felicitaciones! Adivino el jugador")
        break