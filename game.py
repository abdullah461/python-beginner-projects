from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  #list to represent the 3 * 3 board
        self.current_winner = None #keep track of the current winner

    def print_board(self):
        
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + '| '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():

        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def avail_moves(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_Squares(self):
        return self.board.count(' ') 

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False 

    
    def winner(self, square, letter):

        row_index = square // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row ]):
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            
            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

        
def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter

    while game.empty_squares():
        
        if letter =='O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
                    
        #function that make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print('') #empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
                
            #alternate letters
            letter = 'O' if letter == 'X' else 'X'
        #timer
        time.sleep(1)

    if print_game:
        print('its a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)
        