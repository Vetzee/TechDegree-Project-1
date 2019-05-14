# imports built in modules
import random
import time

# displays on screen the opening 'welcome'
print("-" * 28)
print("Welcome to the Guessing Game!")
print("-" * 28)

# global list for the high scores, if placed inside function it will
# delete the last attempt count
high_scores = []


# where most of the magic happens
def start_game():
    random_number = random.randint(1, 10)  # ai picks random number
    attempts = 1  # you can't have 0 attempts right?
    game = True  # every game is true until you quit no

    while game:  # truthy

        # inside try block because that's what some humans do. they try
        try:
            player_guess = int(input("Guess a number from 1-10: "))

        # we also enjoy breaking things...sometimes...
        except ValueError:
            print("Oh no, that's not a valid value")

        # then there is those who think mistakes are bad
        else:

            # dis a whole lot of logic, well this whole programs is lol
            if player_guess < 1 or player_guess > 10:
                print("Should be a number between [1-10] Try again")
            elif player_guess > random_number:
                print("It's Lower")
                attempts += 1
            elif player_guess < random_number:
                print("It's Higher")
                attempts += 1
            else:
                print(f"You got it! It took you {attempts} tries.")
                game = False
                high_scores.append(attempts)

    # in case one didn't get enough :)
    player_response = input("Would you like to play again? [y]es/[n]o: ")
    player_response = player_response.lower()
    if player_response == 'y' or player_response == 'yes':
        print(f"\nCURRENT HIGH-SCORE: {min(high_scores)}\n")  # lets go Esports
        start_game()  # loopy loop

    # bye have great time
    else:
        print("\nHope you enjoyed playing, see you next time")
        time.sleep(4)  # cuz im fancy jk


# would have been nice if this was explained earlier, but we here to learn right
if __name__ == '__main__':
    start_game()

# fyi i'll try to be more professional about my comments next time, unless is coo?
