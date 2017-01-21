# This is the guess the number game
import random

print('Hello, player, what is your name?')

player_name = input();

print('Well, {0}, let\'s play the "Guess the Number" game'.format(player_name))

guesses_taken = 0

while guesses_taken < 6:
    print('Take a guess')

    guesses_taken += 1



