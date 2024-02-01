
class TicTacToeBoard:
    def __init__(self):
        self.board = [" "] * 9

    def print_board(self):
        print("///////////")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("///////////")

    def check_winner(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if all(self.board[i * 3 + j] == player for j in range(3)) or \
                    all(self.board[i + j * 3] == player for j in range(3)):
                return True
        if all(self.board[i] == player for i in [0, 4, 8]) or all(self.board[i] == player for i in [2, 4, 6]):
            return True
        return False

    def is_board_full(self):
        return " " not in self.board
