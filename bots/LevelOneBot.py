import random
from utils import TicTacToeBoard


class LevelOneBot:
    def __init__(self, symbol, verbose=False):
        self.symbol = symbol
        self.verbose = verbose

    def make_move(self, board):
        available_moves = [i for i in range(9) if board[i] == " "]
        random_move = random.choice(available_moves)
        board[random_move] = self.symbol
        if self.verbose:
            print(f"{self.symbol} chose to move to {random_move + 1}")
        return board
