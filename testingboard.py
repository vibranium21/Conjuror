import chess
import chess.svg
from movegeneration import Minimax_Get_Move

def print_board(board):
    print(board)

def play_game():
    board = chess.Board()
    print_board(board)

    while not board.is_game_over():
        
        move = Minimax_Get_Move(board, 5, chess.WHITE)
        board.push(move)

        print_board(board)


play_game()
