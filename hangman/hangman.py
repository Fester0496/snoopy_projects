import random

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
