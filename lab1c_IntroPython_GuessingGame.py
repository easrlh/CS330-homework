def main():
    number = 10
    turn = 0
    guesses = []
    name = input("What is your name? ")
    print("Hello ", name, ". You will have 7 chances to guess a number between 0 and 10.")
    while guess != number and turn < 7:
        guess = input("What number would you like to guess? ")
        guesses.append(guess)
        turn += turn
    if guess == number:
        print("You win ", name, "!")
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
