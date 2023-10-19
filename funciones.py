import random
    
def add_digit(number):
    add = 0
    number = abs(number)
    while number!=0:
        digit = number % 10
        add += digit
        number //= 10
    return add

def summation(numbers):
    add = 0
    for n in numbers:
        add += n
    return add

def rand_player(players):
    num = random.randint(0, len(players))

    return players[num]