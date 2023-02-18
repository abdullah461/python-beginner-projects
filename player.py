import random
import math


class Player:
    def __init__(self, letter):
        self.letter = letter

    # all players should get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.avail_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "\'s turn. Input move (0=8):")

            try:
                val = int(square)
                if val not in game.avail_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square try again.')
        return val

