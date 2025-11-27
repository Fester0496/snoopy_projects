import random

print("======================\nWelcome to Tic Tac Toe\n======================")
print("Instructions: each number responds to each position\n7|8|9\n4|5|6\n1|2|3")


empty_list = [" ", " ", " ",
              " ", " ", " ",
              " ", " ", " "]


def possible_outcomes(empty_list):
    wins = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in wins:
        if empty_list[a] == empty_list[b] == empty_list[c] and empty_list[a] != " ":
            return empty_list[a]


def board_print(empty_list):
    print(f"{empty_list[6]} | {empty_list[7]} | {empty_list[8]}")
    print("--+---+--")
    print(f"{empty_list[3]} | {empty_list[4]} | {empty_list[5]}")
    print("--+---+--")
    print(f"{empty_list[0]} | {empty_list[1]} | {empty_list[2]}")
    print("=========")

while True:
    user_input = int(input("Choose a number/space on the board: "))
    empty_list[user_input - 1] = "X"
    board_print(empty_list)

    winner = possible_outcomes(empty_list)
    if winner:
        print("Player wins")
        break


    computer_input = random.randint(1, 9)
    empty_list[computer_input - 1] = "O"
    board_print(empty_list)

    winner = possible_outcomes(empty_list)
    if winner:
        print("Computer wins")
        break