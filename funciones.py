import random
import math
    
def add_digit(number):
    # Creo variable add donde se van a ir sumando los digitos del número
    add = 0
    # Paso a valor absoluto para evitar errores en número negativos
    number = abs(number)
    while number!=0:
        # Si numero es distinto de 0, entro al bucle
        digit = number % 10 # Digit es igual al resto del numero divivido 10
        add += digit 
        number //= 10 # Divido el número por 10 
    return add

def summation(numbers):
    # Creo variable para ir sumando en ella
    add = 0
    for n in numbers:
        # Recorro la lista, y voy sumando cada elemento en add
        add += n
    return add

def rand_player(players):
    # Obtengo un número random, y devuelvo al jugador que ocupa esa posición
    num = random.randint(0, len(players))

    return players[num]

def valid_dni(num_dni):
    # Verifica que la cantidad de digitos del número dni este entre 7 y 8
    if len(num_dni)<=8 and len(num_dni)>=7:
        return True
    else:
        return False
    
def get_last_word(phrase):
    # Divido la frase en una lista que contiene las palabras 
    words = phrase.split()
    if words:
        # Si la lista no es vacia, devuelvo la ultima palabra
        return words[-1]
    else:
        return ""

def get_first_word(phrase):
    # Obtengo la primer palabra de la cadena, desde la posicion 0, hasta encontrar el primer espacio 
    first_word = phrase[0 : phrase.find(" ")]

    return first_word

def is_multiple(n1,n2):
    # Si n1 es mayor a n2, y el resto de dividir n1 por n2 es 0, devuelvo True, en caso contrario devuelvo False
    return n1 > n2 and n1 % n2 == 0

def average_temperature(max,min):
    # Sumo las temperaturas y las divido por 2 para devolver el promedio de las mismas
    return round((max+min)/2 , 1)

def space_phrase(phrase):
    # Se ingresa un espacio entre todas las letras que antes estaban juntas
    new_phrase = phrase.replace(""," ")
    return new_phrase

def max_min(numbers):
    # Creo una lista
    list_max_min = []
    # Saco el maximo y minimo de la lista enviada por parametro
    num_max = max(numbers)
    num_min = min(numbers)
    # Ingreso los valor num_max y num_min a la nueva lista
    list_max_min.append(num_max)
    list_max_min.append(num_min)

    return list_max_min

def area_circum(rad):
    # Creo lista
    list_circle = []
    # Calculo area y circunferencia y las agrego a la lista
    list_circle.append(math.pi * rad**2)
    list_circle.append(2 * math.pi * rad)

    return list_circle

def login(user, password):
    # Variable de numero de intento
    attempts = 0
    
    if user == "usuario1" and password == "asdasd":
        # Si user y password coinciden con lo deseado, sumo un intento y devuelvo verdadero
        attempts +=1
        return [True, attempts]
    else:
        # En caso que no se cumplan las condiciones sumo el intento y devuelvo False
        attempts += 1
        return [False, attempts]
    
def discount(price):
    # Creo una lista con el calculo del descuento aplicado a cada par key, value 
    new_price = [key - (key * value) for key, value in price.items()]
    return new_price
    
def duplicate(num1):
    return num1 * 2

def new_list (duplicate, numbers):
    new_numbers = []

    for n in numbers:
        # A cada numero de la lista lo envio a la funcion duplicate y lo guardo en la nueva lista
        new_numbers.append(duplicate(n))
    
    return new_numbers

def dict_word (phrase):
    word_len = {}
    words = phrase.split()

    for w in words:
        word_len.update({w : len(w)})
    
    return word_len

def vect_module(x,y=0,z=0):
    module = math.sqrt(x**2 + y**2 + z**2)
    return round(module, 2)

def prime_number(num):
    count = 0
    if num % 2 == 0:
        half = num // 2
    else:
        half = (num-1) // 2

    for n in range(2,half+1):
        if num % n ==  0:
            count += 1
    
    if count > 0:
        return False
    else:
        return True
    
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num -1)
    
def find_digit(num,search):
    count = 0

    for n in num:
        if n == search:
            count += 1
        
    return count

def show_list(bingo_card):
    # Funcion para mostrar una lista de listas
    for r in bingo_card: 
        for e in r:
            print(f"{e:>3}", end = " ")
        print()

def bingo(row):
    # Declaro un contador
    count = 0
    for e in row:
        if e == "X":
            # Si el elemento es igual a X, aumento el contador
            count += 1
    if count == 5:
        # Si el contador es igual a 5 devuelvo True
        return True
    else: 
        return False



