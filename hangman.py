from random import randrange
def picking_word_to_guess():
    """This function randomly selects one of the 3 pre-defined words."""
    pick = randrange(3)
    if pick == 0:
        word_to_guess = 'journey'
    elif pick == 1:
        word_to_guess = 'planet'
    elif pick == 2:
        word_to_guess = 'friend'
    return word_to_guess

def default_status(chosen_word):
    """This function creates the default status for the game, a string which consists of as many "_" as the chosen word."""
    print(chosen_word)
    def_status = '_' *len(chosen_word)
    return def_status

word = picking_word_to_guess()
print(default_status(word))