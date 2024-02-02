import random
from utils import TicTacToeBoard
from utils import opposite_symbol


class LevelThreeBot:
    def __init__(self, symbol, verbose=False):
        self.symbol = symbol
        self.verbose = verbose
        self.board = TicTacToeBoard()

    def make_move(self, board):
        self.board.board = board
        available_moves = [i for i in range(0, 9) if board[i] == " "]

        # Check if the bot can win in the next move
        for move in available_moves:
            temp_board = TicTacToeBoard()
            temp_board.board = board.copy()
            temp_board.board[move] = self.symbol
            if temp_board.check_winner(self.symbol):
                board[move] = self.symbol
                if self.verbose:
                    print(f"{self.symbol} thought it will win by moving to {move + 1}")
                return board

        # Check if the opponent can win in the next move
        for move in available_moves:
            temp_board = TicTacToeBoard()
            temp_board.board = board.copy()
            temp_board.board[move] = opposite_symbol(self.symbol)
            if temp_board.check_winner(opposite_symbol(self.symbol)):
                board[move] = self.symbol
                if self.verbose:
                    print(f"{self.symbol} stopped {opposite_symbol(self.symbol)} by moving to {move + 1}")
                return board

        # If the bot cannot win in the next move, make a random move
        random_move = random.choice(available_moves)
        board[random_move] = self.symbol
        if self.verbose:
            print(f"{self.symbol} chose to move to {random_move + 1}")
        return board
