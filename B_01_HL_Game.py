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


# checks for an integer more than 0 (allows <enter>)
def int_check(question):

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


# Main Routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

print("🔼🔼🔼 Welcome to the Higher Lower Game 🔽🔽🔽")
print()

want_instructions = yes_no("Do you wan to read the instructions? ")

# checks users yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds do you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n Round {rounds_played} (Infinite mode) "
    else:
        rounds_heading = f"\n 🕐🕐🕐 Round {rounds_played + 1} of {num_rounds} 🕐🕐🕐"

    print(rounds_heading)
    print()
