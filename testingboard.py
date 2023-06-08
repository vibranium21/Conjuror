import chess
import chess.svg
from movegeneration import Minimax_Get_Move
import math

def print_board(board):
    print(board)

def play_game():
    board = chess.Board()
    print_board(board)

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = Minimax_Get_Move(board, 5, chess.WHITE, -2000000, math.inf)
        else:
            # Get the move from the other player or external engine
            move_str = input("Enter your move: ")
            move = chess.Move.from_uci(move_str)

        board.push(move)
        print_board(board)

play_game()
