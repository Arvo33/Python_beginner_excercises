# Ex 8
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
            while True:
                user_input = input('What is your move?\n(insert: s for scissors, r for rock or p for paper)\n').lower()
                if user_input not in ['s', 'r', 'p']:
                    print('Inserted unapropriate value. Try again.')
                    continue
                else:
                    return user_input


class Game:

    def __init__(self, players_list):
        self.moves_dict = {'s': [1,'Scissors'], 'r': [2, 'Rock'], 'p': [3, 'Paper']}
        self.players = list(players_list)
        self.moves_comparrison_list = []

    def gameplay(self):
        while True:
            self.moves()
            winner = self.result()
            if winner is None:
                self.moves_comparrison_list.clear()
                print('Draw!\n')
                continue
            print('\n{} wins! Confratulations!'.format(winner))
            self.moves_comparrison_list.clear()
            if not self.quit_check():
                break


    def moves(self):
        for player in self.players:
            result = player.play()
            self.moves_comparrison_list.append(self.moves_dict[result][0])
            print('{}: {}'.format(player.name, self.moves_dict[result][1]))

    def result(self):

        if self.moves_comparrison_list[0] == self.moves_comparrison_list[1]:
            return None
        elif sum(self.moves_comparrison_list) == 4:
            return self.players[self.moves_comparrison_list.index(1)].name
        else:
            return self.players[self.moves_comparrison_list.index(max(self.moves_comparrison_list))].name


    def quit_check(self):
        while True:
            check = input('\nDo you want to continue?\n(y = yes, n = no)\n').lower()
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
