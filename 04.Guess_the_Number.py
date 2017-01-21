# This is the guess the number game
import random

print('Hello, player, what is your name?')

player_name = input();

print('Well, {0}, let\'s play the "Guess the Number" game'.format(player_name))

secret_number = random.randint(1, 20)

guesses_taken = 0

while guesses_taken < 6:
    print('Take a guess')
    guess = input()
    guess = int(guess)

    if secret_number > guess:
        print("Your guess is too low")
    elif secret_number < guess:
        print("Your guess is too hight")
    else:
        print("You are right!!!")

    guesses_taken += 1



