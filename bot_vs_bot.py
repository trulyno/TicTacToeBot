from bots.LevelOneBot import LevelOneBot
from bots.LevelTwoBot import LevelTwoBot
from bots.LevelThreeBot import LevelThreeBot
from utils import TicTacToeBoard


def play_bot_vs_bot():

    print("How many games to play?")
    num_games = int(input("> "))

    print("Concise mode?(yes/no)")
    concise_mode = input("> ").lower() == "yes"
    x_wins = 0
    o_wins = 0
    draws = 0

    display_board = False
    if not concise_mode:
        print("Display board?(yes/no)")
        display_board = input("> ").lower() == "yes"

    print("Select X bot difficulty(1-3)")
    bot_difficulty = int(input("> "))
    match bot_difficulty:
        case 1:
            bot1 = LevelOneBot("X", not concise_mode)
        case 2:
            bot1 = LevelTwoBot("X", not concise_mode)
        case 3:
            bot1 = LevelThreeBot("X", not concise_mode)

    print("Select O bot difficulty(1-3)")
    bot_difficulty = int(input("> "))
    match bot_difficulty:
        case 1:
            bot2 = LevelOneBot("O", not concise_mode)
        case 2:
            bot2 = LevelTwoBot("O", not concise_mode)
        case 3:
            bot2 = LevelThreeBot("O", not concise_mode)

    print(f"Tic Tac Toe - Bot vs Bot! {num_games} games")

    i = 1
    while i <= num_games:
        tic_tac_toe_board = TicTacToeBoard()
        while True:
            tic_tac_toe_board.print_board(display_board)

            # Bot 1 move
            tic_tac_toe_board.board = bot1.make_move(tic_tac_toe_board.board)

            if tic_tac_toe_board.check_winner(bot1.symbol):
                tic_tac_toe_board.print_board(display_board)
                if not concise_mode:
                    print(f"{bot1.symbol} wins! Bot 1 is victorious!")
                x_wins += 1
                break
            elif tic_tac_toe_board.is_board_full():
                tic_tac_toe_board.print_board(display_board)
                if not concise_mode:
                    print("It's a tie!")
                draws += 1
                break

            tic_tac_toe_board.print_board(display_board)

            # Bot 2 move
            tic_tac_toe_board.board = bot2.make_move(tic_tac_toe_board.board)

            if tic_tac_toe_board.check_winner(bot2.symbol):
                tic_tac_toe_board.print_board(display_board)
                if not concise_mode:
                    print(f"{bot2.symbol} wins! Bot 2 is victorious!")
                o_wins += 1
                break
            elif tic_tac_toe_board.is_board_full():
                tic_tac_toe_board.print_board(display_board)
                if not concise_mode:
                    print("It's a tie!")
                draws += 1
                break
        i += 1

    print("Results:")
    print(f"X wins: {x_wins}({x_wins * 100 / num_games}%)")
    print(f"O wins: {o_wins}({o_wins * 100 / num_games}%)")
    print(f"Draws: {draws}({draws * 100 / num_games}%)")


if __name__ == "__main__":
    play_bot_vs_bot()
