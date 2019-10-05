# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a
# message of congratulations to the winner, and ask if the players want to start a new game)
# Remember the rules:
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock
#
# EDIT: I want one of the players to be a computer

from random import choice


class Player:

    def __init__(self, computer=False):
        self.computer = computer
        if self.computer:
            self.name = 'Computer'
        else:
            self.name = input('Enter you name: ')

    def play(self):
        if self.computer:
            return choice(['s', 'r', 'p'])
        else:
            return input('What is your move?\n(insert: s for scissors, r for rock or p for paper)\n')


class Game:

    def __init__(self, players_list):
        self.moves_dict = {'s': [1,'Scissors'], 'r': [2, 'Rock'], 'p': [3, 'Paper']}
        self.players = list(players_list)
        self.moves_comparrison_list = []

    def gameplay(self):
        while True:
            self.moves()
            self.result()
            self.moves_comparrison_list.clear()
            if not self.quit_check():
                break


    def moves(self):
        for player in self.players:
            result = player.play().lower() # poprawić
            self.moves_comparrison_list.append(self.moves_dict[result][0])
            print('{}: {}'.format(player.name, self.moves_dict[result][1]))

        if self.moves_comparrison_list[0] == self.moves_comparrison_list[1]:
            pass

    def result(self):
        winner = ''
        if sum(self.moves_comparrison_list) == 4:
            winner = self.players[self.moves_comparrison_list.index(3)].name
        else:
            winner = self.players[self.moves_comparrison_list.index(max(self.moves_comparrison_list))].name
        print('{} wins! Confratulations!'.format(winner))

    def quit_check(self):
        while True:
            check = input('Do you want to continue?\n(y = yes, n = no)\n').lower()
            if check != 'y' and check != 'n':
                print('Inserted unapropriate value. Try again.')
                continue
            elif check == 'y':
                return True
            else:
                return False


if __name__ == '__main__':
    p1 = Player()
    p2 = Player(True)
    game = Game([p1, p2])
    game.gameplay()
