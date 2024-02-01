import random
from utils import TicTacToeBoard


class LevelTwoBot:
    def __init__(self, symbol):
        self.symbol = symbol
        self.board = TicTacToeBoard()

    def make_move(self, board):
        self.board.board = board
        available_moves = [i for i in range(0, 9) if board[i] == " "]

        # Check if the bot can win in the next move
        for move in available_moves:
            temp_board = TicTacToeBoard()
            temp_board.board = board.copy()
            temp_board.board[move] = self.symbol
            if temp_board.check_winner(temp_board):
                board[move] = self.symbol
                return board

        # If the bot cannot win in the next move, make a random move
        random_move = random.choice(available_moves)
        board[random_move] = self.symbol
        return board
