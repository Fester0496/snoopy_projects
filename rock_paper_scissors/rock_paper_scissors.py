import random

print("ROCK PAPER SCISSORS")

choices = ["rock", "paper", "scissors"]
numbers_to_words = {1: "rock", 2: "paper", 3: "scissors"}


while True:
    computer_choice = random.choice(choices)
    num = int(input("Choose 1 for rock 2 for paper 3 for scissors or 0 to quit: "))

    if num == 0:
        print("Thank you for playing")
        break

    user_input = numbers_to_words.get(num, None)

    if user_input is None:
        print("Invalid input try again")
        continue

    if user_input == computer_choice:
        print(
            "You chose:", user_input, "Computer chose:", computer_choice, "It's a tie"
        )
    elif user_input == "rock" and computer_choice == "scissors":
        print("You chose:", user_input, "Computer chose:", computer_choice, "You win")
    elif user_input == "paper" and computer_choice == "rock":
        print("You chose:", user_input, "Computer chose:", computer_choice, "You win")
    elif user_input == "scissors" and computer_choice == "paper":
        print("You chose:", user_input, "Computer chose:", computer_choice, "You win")
    else:
        print(
            "Computer chose:",
            computer_choice,
            "You chose:",
            user_input,
            "Computer wins",
        )
    if user_input is None:
        print("Invalid input try again")
        continue
