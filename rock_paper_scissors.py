from colorama import Fore
import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

again = True

while again:
    player_move = input(Fore.LIGHTWHITE_EX + "Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit(Fore.RED + "Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)

    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.LIGHTGREEN_EX + "You win! ;D")
    elif player_move == computer_move:
        print(Fore.CYAN + "Draw!")
    else:
        print(Fore.RED + "You lose!")

    extra_game = input(Fore.YELLOW + "Type [yes] to Play Again or [no] to quit: ")

    if extra_game == "no":
        again = False
    elif extra_game == "yes":
        continue
    else:
        print(Fore.RED + "Invalid Input. Try again...")
