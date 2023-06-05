import chess
import chess.svg

def print_board(board):
    print(board)

def play_game():
    board = chess.Board()
    print_board(board)

    while not board.is_game_over():
        #Message to future me: configure line 13 and 14 for bot's move function
        #move = bot.get_move(board)
        #board.push(move)

        print_board(board)

# Call the play_game function to start the game
play_game()
