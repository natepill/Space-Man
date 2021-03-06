import random
import string



display_hangman = ["""
       _________
        |/
        |
        |
        |
        |
        |
        |___
        """,

    """
       _________
        |/   |
        |
        |
        |
        |
        |
        |___
        """,

    """
       _________
        |/   |
        |   (_)
        |
        |
        |
        |
        |___
        """,

    """
       ________
        |/   |
        |   (_)
        |    |
        |    |
        |
        |
        |___
        """,


    """
       _________
        |/   |
        |   (_)
        |   -|
        |    |
        |
        |
        |___
        """,


    """
       _________
        |/   |
        |   (_)
        |   -|-
        |    |
        |
        |
        |___
        """,


    """
       ________
        |/   |
        |   (_)
        |   -|-
        |    |
        |   /
        |
        |___
        """,


    """
       ________
        |/   |
        |   (_)
        |   -|-
        |    |
        |   /-\
        |
        |___
        """]
display_hangman.reverse()



def choose_word():
    word_index = random.randint(0, len(mystery_words) - 1)
    return mystery_words[word_index]


mystery_words = ["magic", "special", "dummy", "astro", "limitation", "hateful", "manipulation","careful"]
letter_list = dict.fromkeys(string.ascii_lowercase, False)
letter_guess = ""




chosen_word = list(choose_word())
# print(chosen_word)
# print("Chosen word is: {}".format(chosen_word))
playing = True
word_to_list = []
chances = 7
hangman_index = 6



def initially_display_word():
    for letter in chosen_word:
        word_to_list.append("_")
    print(word_to_list)


initially_display_word()


def test_letter(guessed_letter):
    index = 0
    for letter in chosen_word:
        if letter == guessed_letter:
            word_to_list[index] = letter

        if letter not in chosen_word:
            print("ELIF STATEMENT")

        index += 1

def check_input(letter_guess):

    good_input = True
    while good_input:

        if len(letter_guess) > 1:
            print("Only one character at a time!")
            break

        if letter_guess.isalpha() == False:
            print("Only alphabet input allowed")
            break

        if letter_list[letter_guess] == True:
            print("You already guessed that letter!")
            break

        return


while playing:

    if word_to_list == chosen_word:
        print("YOU WON!")
        break

    if chances == 0:
        print("YOU LOSE!")
        break

    letter_guess = input("Guess a letter: ")

    check_input(letter_guess)


    if letter_guess.lower() in chosen_word:
        letter_list[letter_guess] = True
        print("Letter Found!")
        test_letter(letter_guess)
        word_string = "".join(word_to_list)
        print(word_string)

    elif letter_guess not in chosen_word:
        print("Not in word")
        print(display_hangman[hangman_index])
        word_string = "".join(word_to_list)
        print(word_string)
        hangman_index -= 1
        chances -= 1
        print("You have {} chances left".format(chances))
