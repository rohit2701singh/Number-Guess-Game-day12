import random

easy_level_attempts = 10
hard_level_attempts = 5

print("welcome to the python number guessing game.")
print("I'm thinking a number between 1 to 100.\nYou have to guess the number in limited attempts based on your choice of difficulty level.")
print("\033[3m" + "\033[4m" + "Hint: 'near the result' means you are either 10 number below or 10 number high.\n" + "\033[0m")


def number_selection():
    return random.choice(range(1, 101))  # use randint(1,100)


chosen_number = number_selection()
# print(f"chosen_number: {chosen_number}\n")

level = input("choose the difficulty level. Type 'e for easy' and 'h for hard': ").lower()


def difficulty_level(user_input):
    if user_input == "e":
        return easy_level_attempts
    elif user_input == "h":
        return hard_level_attempts


attempts = difficulty_level(level)
print(f"you chose '{level}'. You've -{attempts} attempts- to guess the number.")

is_game_over = False
while not is_game_over:
    if attempts < 1:
        is_game_over = True
        print("your attempts are finished. \n💔 YOU LOST.")
    else:
        guessed_number = int(input("guess a number between 1 and 100 :  "))
        if guessed_number == chosen_number:
            is_game_over = True
            print("you guessed the right number.\n🎉 YOU WIN.")


        def remaining_attempts():
            if guessed_number < chosen_number:
                # extra if function is not necessary. you can just print that guess is low.
                if chosen_number - 10 < guessed_number < chosen_number:
                    print("your guess is low but near the result.")
                else:
                    print("your guess is too low.")
            elif guessed_number > chosen_number:
                if chosen_number < guessed_number < chosen_number + 10:
                    print("your guess is high but near the result.")
                else:
                    print("your guess is too high.")
            return attempts - 1

        attempts = remaining_attempts()  # attempts-=1
        print(f"🚨 remaining_attempts: {attempts} 🚨")

print(f"🚩I was thinking about number : {chosen_number}")

