# checks for an integer with optimal upper /
# lower limit and an optimal exit code for infinite mode
# / quiting the game
def int_check(question, low=None, high=None, exit_code=None):

    # If any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # If number need to be more than an
    # Integer (ie: rounds / 'High number')
    elif low is None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # If the number need to be low & high
    else:
        error = (f"Please enter an integer that "
                 f"is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # Checks for an infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is no to low...
            if low is not None and response < low:
                print(error)

            # Check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # If response is valid, return it
            else:
                return response

        except ValueError:
            print(error)


# Guessing Loop

# replace number below with random number between high / low values
secret = 7

# parameters that already exist in base game
low_num = 0
high_num = 10
guess_allowed = 5

# Set guesses used to zero at the start of each round
guesses_used = 0
already_guessed = []

guess = ""

while guess != secret and guesses_used < guess_allowed:

    # ask the user to guest the number
    guess = int_check("Guess: ", low_num, high_num, "xxx")

    # check that they don't want to quit
    if guess == "xxx":
        # set end_game to use so that outer loop can be broken
        end_gamee = "yes"
        break

    # check that guess is not a duplicate
    if guess in already_guessed:
        print(f"You've already guessed {guess}, You've *still* used "
              f"{guesses_used} / {guess_allowed} guesses ")
        continue

    # If it is not a duplicate, add it to the 'already guessed' list
    else:
        already_guessed.append(guess)

    # add one to the number of guesses used
    guesses_used += 1

    # compare the user's guess with the secret number set up feedback statement

    # If we have guesses left...
    if guess < secret and guesses_used < guess_allowed:
        feedback = (f"Too low, please try a higher number. "
                    f"You've used {guesses_used} / {guess_allowed} guesses")
    elif guess > secret and guesses_used < guess_allowed:
        feedback = (f"Too high, please try a lower number, "
                    f"You've used {guesses_used} / {guess_allowed} guesses")

    # when the secret number is guessed, we have three different feedback
    # options {lucky / 'phew' / well done}
    elif guess == secret:

        if guesses_used == 1:
            feedback = "🍀🍀 Lucky! You got it on the first guess. 🍀🍀"
        elif guesses_used == guess_allowed:
            feedback = f"Phew! You got it in {guesses_used} guesses."
        else:
            feedback = f"Well done! You have guessed the secret number in {guesses_used} guesses."

    # if there are no guesses left!
    else:
        feedback = "Sorry - you have no more guesses. You lose this round!"

    # print feedback to the user
    print(feedback)

    # Additional feedback (warn user that they are running out of guesses)
    if guesses_used == guess_allowed - 1:
        print("\n💣💣💣 Careful - you have one guess left! 💣💣💣\n")

print()
print("End of round!")
