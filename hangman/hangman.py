import random

<<<<<<< HEAD
print("Welcome to hangman")
print("Instructions: guess each letter of the word")

word_list = ["apple", "name", "george", "snoopy"]


random_word = random.choice(word_list)
print(random_word)

current_state = ["_"] * len(random_word)
print("".join(current_state))

tries = 0
while True:

    user_input = input("Give me a letter: ")
    tries += 1

    for index, value in enumerate(random_word):
        if value == user_input:
            current_state[index] = value
    print("".join(current_state))

    if "".join(current_state) == random_word:
        print(f"You got it the word was {random_word}")
        break
    elif user_input not in random_word:
        print("Wrong letter try again")
=======


print("Welcome to hangman")
print("Instructions: guess each letter to find the word")


word_list = ["apple", "name", "snoopy"]
random_word = random.choice(word_list)
word_print = ["_"] * len(random_word)
print(random_word)
print("-" * len(random_word))

lives = 2
while True:
    user_input = input("guess a letter ")

    for index, value in enumerate(random_word):
        if user_input == value:
            word_print[index] = value

    if "".join(word_print) == random_word:
        print(f"You got it the word was {random_word}")
        break

    if lives == 0:
        print("0 lives remaining game over")
        break

    if user_input in random_word:
        print("".join(word_print))
        continue
    elif user_input not in random_word:
        print(f"Wrong guess {lives} lives remaining")
        lives -= 1
    else:
        print("Invalid input")
    
    
>>>>>>> 0db323f4229175538d0af444ce7ca4e396ca9292
