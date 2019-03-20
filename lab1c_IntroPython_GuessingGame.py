import random

def main():
    number = random.randint(0, 10)
    turn = 0
    guesses = []
    guess = 100;
    name = input("What is your name? ")
    
    print("Hello ", name, ". You will have 7 chances to guess a number between 0 and 10.")
    
    while guess != number and turn < 7:
        guess = int(input("What number would you like to guess? "))
        if guess <= 10 and guess >= 0:
            guesses.append(guess)
            turn = turn + 1
            if guess == number:
                print("You win ", name,"!")
                print("It took you ", turn, " tries to guess the secret number.")
                print("Your guesses were...")
                for guess in guesses:
                    print("Turn ", guesses.index(guess) + 1, ": ", guess)

            elif turn == 7:
                print("You're out of guesses!")
                print("You guessed...")
                for guess in guesses:
                    print("Turn ", guesses.index(guess) + 1, ": ", guess)
                print("The correct answer was ", number)

        else:
            guess = input("Please enter a digit between 0 and 10!")
            
main()
