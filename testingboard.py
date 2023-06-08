import chess
import chess.svg
from movegeneration import Minimax_Get_Move
import math



def play_game():
    board = chess.Board()
    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move, _ = Minimax_Get_Move(board, 3, chess.WHITE, -2000000, math.inf)
            board.push(move)
        else:
            move = input("Enter your move: ")
            board.push_san(move)
        print(board)

play_game()



