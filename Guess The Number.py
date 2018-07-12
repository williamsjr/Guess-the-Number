import random

#Enter name
def get_name():
    """ NoneType -> str
    Return the name of the player w/ a greeting
    """
    print("What is your name? ")
    name = input()

    if name:
        print("Thanks,",name, "Let's play!")

#generate a random number
def random_number():
    """ (int) -> int

    return a random number from 1 - 100

    """
    return int(random.randint(1, 100))

#determine if guess is close or not
def guess_num():
    """ (int) -> str

    Return a string telling player if their guess is close
    to the random number or not"""
    guess = 0
    guesses_taken = 0
    num = random_number()
    while num != guess:
        guess = int(input('Guess a number between 1 - 100: '))
        guesses_taken += 1
        
        if num > guess:
            print("Guess too low, guess agian: ")
        if num < guess:
            print("Guess too high, guess again: ")
        if num == guess:
            print("Nice job, you guessed the number in" , guesses_taken, "guesses")
            print("Would you like to play again? (yes/no): ")
            play_again = input()

            if play_again == 'yes':
                guess = 0
                guesses_taken = 0
                num = random_number()
                while num != guess:
                    guess = int(input('Guess a number between 1 - 100: '))
                    guesses_taken += 1
        
                    if num > guess:
                        print("Guess too low, guess agian: ")
                    if num < guess:
                        print("Guess too high, guess again: ")
                    if num == guess:
                        print("Nice job, you guessed the number in" , guesses_taken, "guesses")

            elif play_again == 'no':
                exit
                              
            

get_name()
random_number()
guess_num()
