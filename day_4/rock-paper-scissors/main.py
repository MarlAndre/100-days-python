# Write your code below this line 👇
import random

# Keep track of the score until 3 wins
player_score = int(0)
computer_score = int(0)
max_score = 3

while True:

    # Ask player for their choice
    choices = ["rock", "paper", "scissors"]

    player_choice = input("Type 0 for'rock', 1 for 'paper' and 2 for 'scissors'.\n").lower()

    choices_int = int(player_choice)
    player_input = choices[choices_int]
    print(f"You chose {player_input}.")
    print("-------------------------")

    # Computer picks randomly
    choices_length = (len(choices))
    computer_choice = random.randint(0, choices_length - 1)
    computer_input = choices[computer_choice]
    print(f"Computer chose {computer_input}.")
    print("-------------------------")

    # Outcome of the game
    if player_input == computer_input:
        print("It's a tie")
    elif (player_input == "rock" and computer_input == "scissors") or (
            player_input == "scissors" and computer_input == "paper") or (
            player_input == "paper" and computer_input == "rock"):
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print("============================")
    print(f"score: YOU: {player_score} | computer: {computer_score}")
    print("============================")

    # Declare the winner after a few rounds

    if computer_score == max_score:
        print("Computer is DA BEST!")
        break

    if player_score == max_score:
        print("You DA BEST!")
        break