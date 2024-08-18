from random import choice

user_wins = 0
computer_wins = 0
tie = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    # random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = choice(options)
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
        tie += 1

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times. &", tie, "ties.")
print("Goodbye!")