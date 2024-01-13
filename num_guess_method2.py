import random

level = {
    "easy": 10,
    "hard": 5,
}

print("welcome to the number guessing game")
print("I'm thinking about a number between 1 and 100.\n")

guessed_number = random.randint(1, 100)
# print(guessed_number)

user_level = input("choose a difficulty. Type 'easy' or 'hard': ").lower()
print(f"you've {level[user_level]} attempts to guess the number.\n")

user_total_chance = level[user_level]
game_finished = False
while user_total_chance > 0 and not game_finished:

    user_guess = int(input("Guess a number:"))

    if guessed_number == user_guess:
        print(f"you got it.\nyou've {user_total_chance} attempts remaining.\n")
        game_finished = True
    else:
        if guessed_number < user_guess:
            print("you got it wrong. You guessed Too high.")
        elif guessed_number > user_guess:
            print("you got it wrong. You guessed Too low.")

        user_total_chance -= 1
        print(f"you've {user_total_chance} attempts remaining.\n")

print(f"I was thinking about the number: {guessed_number}")
