# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them
# whether they guessed too low, too high, or exactly right.
#
# Extras:
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

from random import randint


class Game:
    def __init__(self, player):
        self.player = player
        self.random_number = 0
        self.user_number = 0

    def choose_random_number(self):
        return randint(1, 9)

    def play(self):
        print('Let\'s start a game\n')
        self.random_number = self.choose_random_number()
        self.user_number = self.player.guess()

    def check(self):
        if self.user_number == self.random_number:
            return True
        else:
            return False


class Player:

    def guess(self):
        return int(input('Choose your number: '))



