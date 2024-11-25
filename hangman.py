from random import randrange
def picking_word_to_guess():
    pick = randrange(3)
    if pick == 0:
        word_to_guess = 'journey'
    elif pick == 1:
        word_to_guess = 'planet'
    elif pick == 2:
        word_to_guess = 'friend'
    return word_to_guess

print(picking_word_to_guess())