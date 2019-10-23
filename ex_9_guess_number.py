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
        print('Let\'s start a game!\n')
        while True:
            count = 0
            self.user_number = 0
            self.random_number = self.choose_random_number()
            while self.random_number != self.user_number:
                self.user_number = self.player.guess()
                count += 1
                if not self.user_number:
                    print('Game over.')
                    exit()
                if self.check() > 0:
                    print('Your number is greater then selected number.')
                    continue
                elif self.check() < 0:
                    print('Your number is less then selected number')
                    continue
            print('Congratulaions! You guessed right number! Guesses: {}.'.format(count))
            if not self.player.continue_game():
                print('Game over.')
                break

    def check(self):
        return self.user_number - self.random_number


class Player:

    def guess(self):
        while True:
            user_input = input('Choose your number from 1 to 9 or type "exit" to quit\n: ').lower()
            if user_input == 'exit':
                return 0
            elif 0 < int(user_input) < 10:
                return int(user_input)
            else:
                print('Number out of possible range. Ty again.')

    def continue_game(self):
        while True:
            user_input = input('Do you want to continue?\n(type "y" for yes; "n" or "exit" for no)\n: ').lower()
            if user_input == 'y':
                return True
            if user_input == 'n' or user_input == 'exit':
                return False
            else:
                print('Inserted unappriopriate value.')


if __name__ == '__main__':
    player = Player()
    game = Game(player)
    game.play()
