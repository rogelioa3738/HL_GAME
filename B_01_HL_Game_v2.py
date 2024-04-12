import math
import random

# checks users yes (y) or no (n)


def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats it if user don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''

**** Instructions ****

To begin, decide on a score goal (eg: The first one to get a score of 50 wins)

For each round of the game, you win points by rolling the dice.
The winner of the round is the one who gets 13 (or slightly less).

If you win the round, then your score will increase by the number of points that you earned. If you first roll of two
dice is double (eg: both dice show three), then your score will be DOUBLE the number of points.

If you lose the round, then you don't get any points.

If you tie (eg: you both get a score of 11, then you will have 11 adding to your score).

Your goal is to try to get to the target score before the computer.

Good luck.

    ''')


# checks for an integer with optimal upper /
# lower limit and an optimal exit code for infinite mode
# / quiting the game
def int_check(question, low=None, high=None, exit_code=None):

    while True:

        error = "Please enter and integer that is 1 or more."

        to_check = input(question)

        # check for an infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is greater than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# calculate the number of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
end_game = "no"
feedback = ""

game_history = []
all_scores = []

print("🔼🔼🔼 Welcome to the Higher Lower Game 🔽🔽🔽")
print()

want_instructions = yes_no("Do you wan to read the instructions? ")

# checks users yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# ask user if they want to calculate the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params == "yes":
    low_num = 0
    high_num = 10

# allow user to choose high / low number
else:
    low_num = int_check("Low Number? ")
    high_num = int_check("High number? ", low=low_num+1)

# calculate the maximum number of guesses based on the low and high number
guesses_allowed = calc_guesses(low_num, high_num)

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played + 1} (Infinite mode) "
    else:
        rounds_heading = f"\n 🕐🕐🕐 Round {rounds_played + 1} of {num_rounds} 🕐🕐🕐"

    print(rounds_heading)

    # Round starts here
    # Set guesses used to zero at the start of each round
    guesses_used = 0
    already_guessed = []

    # Choose a 'secret' number between the low and high number
    secret = random.randint(low_num, high_num)

    guess = ""
    while guess != secret and guesses_used < guesses_allowed:

        # ask the user to guess the number...
        guess = int_check("Guess: ", low_num, high_num, "xxx")

        # check that they don't want to quit
        if guess == "xxx":
            # set end_game to use that outer loop can be broken
            end_game = "yes"
            break

        # check that guess is not a duplicate
        if guess in already_guessed:
            print(f"You've already guessed {guess}, You've *still* used "
                  f"{guesses_used} / {guesses_allowed} guesses")

    print()

    # Rounds ends here

    # if the user has entered exit code, end game!!
    if end_game == "yes":
        break

    rounds_played += 1

    # Add round result to the game history
    history_feedback = (f"Round {rounds_played}: {feedback}"
                        f"")

# Game loop ends here

# check users have played at least one round
# before calculating statistics.
if rounds_played > 0:
    # Game History / Statistics area

    # Calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output the statistics
    print("\n🎆🎆🎆 Statistics 🎆🎆🎆")
    print(f"Best:{best_score} | Worst:{worst_score} | Average:{average_score:.2} ")
    print()

    # Display the game history on request
    see_history = yes_no("Do you want to see the game history? ")
    if see_history == "yes":
        print("\n ⌛⌛⌛ Game History ⌛⌛⌛")

        for item in game_history:
            print(item)
