from bots.LevelTwoBot import TicTacToeBot
from utils import TicTacToeBoard


def get_player_choice():
    while True:
        try:
            choice = int(input("Enter a number from 1 to 9 to make your move (or 0 to reset the game): "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_vs_bot():
    player = "X"
    bot = TicTacToeBot("O")
    tic_tac_toe_board = TicTacToeBoard()

    while True:
        print("Tic Tac Toe Game!")

        while True:
            tic_tac_toe_board.print_board()

            choice = get_player_choice()

            if choice == 0:
                print("Game reset.")
                tic_tac_toe_board = TicTacToeBoard()
                break

            if 1 <= choice <= 9 and tic_tac_toe_board.board[choice - 1] == " ":
                tic_tac_toe_board.board[choice - 1] = player

                if tic_tac_toe_board.check_winner(player):
                    tic_tac_toe_board.print_board()
                    print(f"{player} wins!")
                    tic_tac_toe_board = TicTacToeBoard()
                    break
                elif tic_tac_toe_board.is_board_full():
                    tic_tac_toe_board.print_board()
                    print("It's a tie!")
                    tic_tac_toe_board = TicTacToeBoard()
                    break

                # player = "X" if player == "O" else "O"
                tic_tac_toe_board.board = bot.make_move(tic_tac_toe_board.board)

                if tic_tac_toe_board.check_winner(bot.symbol):
                    tic_tac_toe_board.print_board()
                    print(f"{bot.symbol} wins! The bot is victorious!")
                    tic_tac_toe_board = TicTacToeBoard()
                    break
                elif tic_tac_toe_board.is_board_full():
                    tic_tac_toe_board.print_board()
                    print("It's a tie!")
                    tic_tac_toe_board = TicTacToeBoard()
                    break
            elif choice != 0:
                print("Invalid move. The chosen slot is already taken. Try again.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            tic_tac_toe_board = TicTacToeBoard()
            break


if __name__ == "__main__":
    play_vs_bot()
