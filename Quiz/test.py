import numpy as np

class TicTacToe:

    def __init__(self):
        self.board = np.zeros((3,3)) # initialize empty board
        self.player = 1 # player 1 starts
        self.proof_number = 0 # initialize proof number as 0

    def move(self, x, y):
        if self.board[x][y] == 0: # check if cell is empty
            self.board[x][y] = self.player
            self.player = 2 if self.player == 1 else 1 # switch player
            return True
        else:
            return False

    def is_game_over(self):
        # check rows, columns, and diagonals for a win
        for i in range(3):
            if (self.board[i, :] == self.player).all() or (self.board[:, i] == self.player).all():
                return True
        if (self.board.diagonal() == self.player).all() or (np.fliplr(self.board).diagonal() == self.player).all():
            return True
        return False

    def proof_number_search(self):
        if self.is_game_over():
            self.proof_number = 0 # if game is over, proof number is 0
        else:
            min_proof_number = float('inf')
            for x in range(3):
                for y in range(3):
                    if self.board[x][y] == 0:
                        self.move(x, y)
                        min_proof_number = min(min_proof_number, self.proof_number_search())
                        self.board[x][y] = 0
                        self.player = 2 if self.player == 1 else 1
            self.proof_number = min_proof_number + 1
        return self.proof_number

game = TicTacToe()
print(game.proof_number_search())
