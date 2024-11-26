"""Bonus task Game time! Let’s create a hangman game together 
The game should look like this. Separate the project into multiple functions, take care of good descriptive names and write comments (for future you). You should also put everything to git after every step. 
• Computer will randomly choose a word (as a beginning out of 3 options). Also for simplicity use lower case and only words where a letter is used only once. Eg. Mentoring or Pyladies :)
• Default setting of game “status” is a string (or a list) with that many underscores as there are letters in the chosen word. 
• Default setting of unsuccessful tries is zero. (as a counter of guesses) • Keep repeating: 
o Ask the player for a letter. 
o If the letter is in the chosen word, replace corresponding 
underscores with letters in the game status. Write a function for this. 
o If the letter is not present, add one to unsuccessful tries. 
o Print out the game “status” – string with underscores and already revealed letters or still just underscores. 
o If in the string are no underscores, congratulate a player and end the game. 
o Print out the number of unsuccessful tries and (if you want) print out the corresponding picture of a hangman. 
o If the number of unsuccessful tries is 9 or higher, the player loses the game and ends the game."""

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
    def_status = '_' *len(chosen_word)
    return def_status

def evaluating(current_status, unsuccessful_tries):
    """This function evaluates if the game should end or not."""
    if "_" not in current_status:
        print('Congratulations!')
        return 'end'
    elif unsuccessful_tries >= 9:
        print('Unfortunately you lost!')
        return 'end'
    else:
        return 'go'

def letter_position(picked_letter, selected_string):
    """This function returns the position of the desired letter in the word to guess"""
    for i in range(len(selected_string)):
        if selected_string[i] == picked_letter:
            return i
        else:
            pass

def update_status(letter, word_to_guess, status):
    pos = letter_position(letter, word_to_guess)
    updated_status = status[:pos] + letter + status[(pos + 1):] 
    return(updated_status)

def hangman_game():
    word_to_guess = picking_word_to_guess()
    starting_status = default_status(word_to_guess)
    print(starting_status)
    unsuccessful_tries = 0
    status = starting_status
    while evaluating(status, unsuccessful_tries) == 'go':
        letter = input("Guess a letter: ")
        if letter in word_to_guess:
            status = update_status(letter, word_to_guess, status)
            print(status)

        else:
            unsuccessful_tries += 1
            print(f'Unsuccessful tries: ', unsuccessful_tries)
            

#tries = 2
#word1 = "feiensg"
#now_stat = "_______"
#one_guess(word1, tries, now_stat)

#print(evaluating(word1, tries))

#word = picking_word_to_guess()
#print(default_status(word))

hangman_game()