# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you want to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""
"""
I am a comment


"""
# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like random and time packages we've discussed about)
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

import random

print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")
rock = 1
paper = 2
scissors = 3
player1 = input("hello please enter your name")
player2 = "computer"

while True:
    user = input(f"{player1} please choose, 1 for rock , 2 for paper , 3 for scissors")
    computer = random.randint(1, 3)
    if user.isalpha() or int(user) not in range(1, 4):
        print("invalid input")
    else:
        user = int(user)
        if user == rock and computer == scissors:
            print(f"{player1} is the winner")
        elif user == scissors and computer == paper:
            print(f"{player1} is the winner")
        elif user == paper and computer == rock:
            print(f"{player1} is the winner")
        elif user == computer:
            print("its a tie")
        else:
            print(f"{player2} is the winner")
        game = input("do you want to play again? y/n.\n")
        if game == 'y':
            print("new game is begin")
        else:
            break

