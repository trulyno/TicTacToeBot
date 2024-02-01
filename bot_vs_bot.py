from bots.LevelOneBot import LevelOneBot
from bots.LevelTwoBot import LevelTwoBot
from utils import TicTacToeBoard


def play_bot_vs_bot():
    bot1 = LevelOneBot("X")
    bot2 = LevelTwoBot("O")
    tic_tac_toe_board = TicTacToeBoard()

    print("Tic Tac Toe - Bot vs Bot!")

    while True:
        tic_tac_toe_board.print_board()

        # Bot 1 move
        tic_tac_toe_board.board = bot1.make_move(tic_tac_toe_board.board)

        if tic_tac_toe_board.check_winner(bot1.symbol):
            tic_tac_toe_board.print_board()
            print(f"{bot1.symbol} wins! Bot 1 is victorious!")
            break
        elif tic_tac_toe_board.is_board_full():
            tic_tac_toe_board.print_board()
            print("It's a tie!")
            break

        tic_tac_toe_board.print_board()

        # Bot 2 move
        tic_tac_toe_board.board = bot2.make_move(tic_tac_toe_board.board)

        if tic_tac_toe_board.check_winner(bot2.symbol):
            tic_tac_toe_board.print_board()
            print(f"{bot2.symbol} wins! Bot 2 is victorious!")
            break
        elif tic_tac_toe_board.is_board_full():
            tic_tac_toe_board.print_board()
            print("It's a tie!")
            break


if __name__ == "__main__":
    play_bot_vs_bot()
