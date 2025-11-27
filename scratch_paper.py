import random

print("Welcome to hangman")
print("Instructions: guess each letter of the word")

word_list = ["apple", "name", "george", "snoopy"]
word_to_guess = random.choice(word_list)

current_guess = "_" * len(word_to_guess)

while current_guess != word_to_guess:
    
    print(current_guess)
    print("_" * len(word_to_guess))

    player_input = input("Guess a letter: ").lower()
    show_letter = ""
    for letter in word_to_guess:
        if letter == player_input:
            show_letter += letter
        else:
            show_letter += "_"
    print(show_letter)

    if word_to_guess == show_letter:
        print(f"you got it the word was {word_to_guess}")
        break
    else:
        player_input = input("Guess a letter: ")
    