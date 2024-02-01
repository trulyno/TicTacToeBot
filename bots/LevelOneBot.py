import random
from utils import TicTacToeBoard


class TicTacToeBot:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, board):
        available_moves = [i for i in range(9) if board[i] == " "]
        random_move = random.choice(available_moves)
        board[random_move] = self.symbol
        return board
