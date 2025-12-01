import random



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
    
    