# Simple TicTacToe game in console

import random


def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}     1 | 2 | 3 ")
    print("---|---|---   ---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}     4 | 5 | 6 ")
    print("---|---|---   ---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}     7 | 8 | 9 ")


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i * 3 + j] == player for j in range(3)) or \
                all(board[i + j * 3] == player for j in range(3)):
            return True
    if all(board[i] == player for i in [0, 4, 8]) or all(board[i] == player for i in [2, 4, 6]):
        return True
    return False


def is_board_full(board):
    return " " not in board


def get_player_choice():
    while True:
        try:
            choice = int(input("Enter a number from 1 to 9 to make your move, or 0 to exit the game: "))
            if 1 <= choice <= 9:
                return choice
            elif choice == 0:
                return 0
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def can_win_next_move(board, player):
    for i in range(9):
        if board[i] == " ":
            temp_board = board.copy()
            temp_board[i] = player
            if check_winner(temp_board, player):
                return True
    return False


def play_tic_tac_toe():
    player = "X"
    bot = "O"

    while True:
        board = [" "] * 9
        play_with_bot = input("Do you want to play against the bot? (yes/no): ").lower() == "yes"

        if play_with_bot:
            bot_player = input("Choose the bot's symbol (X/O): ").upper()
            if bot_player != "X" and bot_player != "O":
                print("Invalid input. Bot can only be 'X' or 'O'.")
                continue
            bot = bot_player

        print("Tic Tac Toe Game!")

        while True:
            print_board(board)

            if player == bot and play_with_bot:
                if can_win_next_move(board, bot):
                    # Bot wins in the next move
                    choice = [i + 1 for i in range(9) if board[i] == " " and can_win_next_move(board, bot)][0]
                elif can_win_next_move(board, player):
                    # Block the player from winning
                    choice = [i + 1 for i in range(9) if board[i] == " " and can_win_next_move(board, player)][0]
                else:
                    # Random choice if no winning move
                    choice = random.choice([i + 1 for i in range(9) if board[i] == " "])
            else:
                choice = get_player_choice()

            if choice == 0:
                print("Exiting the game...")
                break

            if board[choice - 1] == " ":
                board[choice - 1] = player

                if check_winner(board, player):
                    print_board(board)
                    print(f"{player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break

                player = "X" if player == "O" else "O"
            else:
                print("Invalid move. The chosen slot is already taken. Try again.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    play_tic_tac_toe()
