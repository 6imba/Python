import random
from words import word_list

def get_word():
    word = random.choice(word_list) 
    return word.upper() 

def play(word):
    word_complition = "_"*len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 #number of body part of hangman
    print("Let's play Hangman !")
    print(display_hangman(tries))
    print(word_complition)
    print("\n")
    while not guessed and tries > 0: #untill we guess a word as at staring to loop guessed is false(alternative while True) and  try is not equal to 0 from 6
        guess = input("Please guess a letter or word : ").upper()

        if len(guess) ==1 and guess.isalpha():
            if guess in guessed_letters :
                print('You have already guessed the letter ',guess)
            elif guess not in word:
                print(guess," is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Good job, ',guess,' is the word.')
                guessed_letters.append(guess)
                blanked_as_list = list(word_complition) 
                indices = [index for index,char in enumerate(word) if char == guess] # list of index(position) of chars(who is esqual to guess) in word
                for index in indices:
                    blanked_as_list[index] = guess
                word_complition = "".join(blanked_as_list)
                if "_" not in word_complition:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word ",guess)
            elif guess != word:
                print(guess," is not in the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print('Not a valid guess.')

        print(display_hangman(tries))
        print(word_completion)
        print('\n')

        if guessed:
            print("Congrats !")
        else:
            print("Try, later !")



def display_hangman(tries):
    stages = [  """
                    -------------
                    |           |
                    |           O
                    |          \ /
                    |           |
                    |          / \
                    |
                    """ ,
                    """
                    -------------
                    |           |
                    |           O
                    |          \ /
                    |           |
                    |          / 
                    |
                    """,
                    """
                    -------------
                    |           |
                    |           O
                    |          \ /
                    |           |
                    |          
                    |
                    """,
                    """
                    -------------
                    |           |
                    |           O
                    |          \ /
                    |           
                    |          
                    |
                    """,
                    """
                    -------------
                    |           |
                    |           O
                    |          \ 
                    |           
                    |          
                    |
                    """,
                    """
                    -------------
                    |           |
                    |           O
                    |          
                    |           
                    |           
                    |
                    """,
                    """
                    -------------
                    |           |
                    |           
                    |          
                    |           
                    |           
                    |
                    """
             ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ".upper() == "Y"):
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()
